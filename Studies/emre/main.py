from sympy import N
from connectify.connect import UnityConnection
from plotify.plot import Plotify
from geofy.geo import Geo
from objectify.object import Object
from particlefy.particle import Particle
import time
import tqdm

x_list = []
y_list = []
z_list = []
particles = []
counter = 0 
last = 0


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
        near_points = object.find_nearly_heights(height)


        if counter == 0:
            for i in range(0,len(near_points[0]),100):
                #particle oluştur 
                particles += [Particle(near_points[1][i],near_points[0][i],height)]
            y_list.append(y)

            
            

        else:

            #print(f"Distance : {abs((y-y_list[-1])/30)}")
            speed=abs(y-y_list[-1])



            y_list.append(y)
            for i in range(len(particles)):
                particles[i].move(speed)

        



        plotify.live_plot(x,y,dted_array,particles,counter)

        

        counter += 1

        


        