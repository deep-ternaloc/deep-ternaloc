from sympy import N
from connectify.connect import UnityConnection
from plotify.plot import Plotify
from geofy.geo import Geo
from objectify.object import Object
from particlefy.particle import Particle
import time
import tqdm
import numpy as np

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
    


    uc.establish_connection()
    dted_array = geo.readAsArray()
    object = Object(dted_array)
    #plotify.plot_contour_map(dted_array)

    
    while True:

        unity_data = uc.receive_data()
        x,y,height = object.find_position(unity_data)



    

        #plotify.plot_object_position(x,y,dted_array)
        near_points,object_height = object.find_nearly_heights(height)


        if counter == 0:
            for i in range(0,len(near_points[0])):
                #particle oluştur 
                height = dted_array[near_points[0][i]][near_points[1][i]]

                particles += [Particle(near_points[1][i],near_points[0][i],height)]
            y_list.append(y)

            
            

        else:

            #print(f"Distance : {abs((y-y_list[-1])/30)}")
            speed=abs(y-y_list[-1])



            y_list.append(y)

            for i in range(len(particles)):
                particles[i].move(speed)
            
            for i in range(len(particles)):

                if (particles[i].y or particles[i].x) > 3600:
                    #print(particles[i].x,particles[i].y, i,range(len(particles)))

                    pop_indexes += [i]
                else:

                    particles[i].measure_height(dted_array)
                    particles[i].update_weight(object_height)
                #print(f"Particle {i} : {particles[i].weight}")
                #print(f"Particle {i} : {particles[i].height}, Object: {height}")



            j = len(pop_indexes) -1
            while j >= 0:
                particles.pop(pop_indexes[j])
                j -= 1


            #np.delete(particles,pop_indexes
            pop_indexes=[]

            #for i in range(len(pop_indexes)):
            #    print(pop_indexes[i])
            #    print(len(particles))
            #    particles.pop(pop_indexes[i])
                #pop_indexes.pop(i)
            #pop_indexes=[]
            if counter > 10:

                resampled_particles = Particle.resample_particles(particles,near_points,dted_array)

                particles = resampled_particles

            

            
            plotify.live_plot(x,y,dted_array,resampled_particles,counter)


        

        

        counter += 1

        


        