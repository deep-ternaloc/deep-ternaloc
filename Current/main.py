from sympy import N
from connectify.connect import UnityConnection
from plotify.plot import Plotify
from geofy.geo import Geo
from objectify.object import Object
from particlefy.particle import Particle
import time
import tqdm
import numpy as np
import random

x_list = []
y_list = []
z_list = []
particles = []
counter = 0 
last = 0
resampled_particles = []
pop_indexes=[]


if __name__ == "__main__":
    uc = UnityConnection()
    plotify = Plotify()
    geo = Geo()


    object_x_list = []
    object_y_list = []

    uc.establish_connection()
    dted_array = geo.readAsArray()
    object = Object(dted_array)
    #plotify.plot_contour_map(dted_array)


    while True:

        unity_data = uc.receive_data()
        x,y,height = object.find_position(unity_data)

        object_x_list.append(x)
        object_y_list.append(y)

        object_height = object.find_nearly_heights(height)


        if counter == 0:
            #for i in range(0,len(near_points[0])):
                #particle oluştur 

                # random x y belirle 
                #dtedde yerini bul
                # particle oluştur

            for i in range (1000):
                x_particle = random.randint(0,3600)
                y_particle = random.randint(0,3600)
                height = dted_array[y_particle][x_particle]

         ## x y yanlis olabilir

                particles += [Particle(x_particle,y_particle,height)]
            y_list.append(y)


            

        else:

            speed=abs(y-y_list[-1])

            y_list.append(y)

            for i in range(len(particles)):
                particles[i].move(speed)

            for i in range(len(particles)):

                if particles[i].y >3600 or particles[i].x>3600 or particles[i].y<0 or particles[i].x <0:


                    pop_indexes += [i]
                else:

                    particles[i].measure_height(dted_array)

                    particles[i].update_weight(object_height,counter)




            j = len(pop_indexes) -1
            while j >= 0:
                particles.pop(pop_indexes[j])
                j -= 1



            pop_indexes=[]
            Particle.pdf_control(particles)

            if counter%10 == 0 and counter != 0:

                
                print(f"Resample öncesi sayi {len(particles)}")
                resampled_particles = Particle.resample_particles(particles,dted_array)
                print(f"Resample sonrasi sayi {len(resampled_particles)}")
                particles = resampled_particles
                #Particle.print_particle_error(object_height,particles)


            
        



        print("Adim Sayisi: {}".format(counter))
        plotify.live_plot(object_x_list,object_y_list,dted_array,particles,counter)
        counter += 1



        #TODO: Y ekseni ekle DONE
        #TODO: PDF Grafik ekle DONE
        #TODO: PDF düzgün mü göster DONE
        #TODO: Adım sayısını değiştir #DONE
        #TODO: Movement and measure sigma değiştir DONE
        
        #TODO: Araca diğer ekseni ekleyebiliriz
        


