from sympy import N
from connectify.connect import UnityConnection
from plotify.plot import Plotify
from geofy.geo import Geo
from objectify.object import Object
from particlefy.particle import Particle
import time
import tqdm


particles = []
counter = 0 


if __name__ == "__main__":
    uc = UnityConnection()
    plotify = Plotify()
    geo = Geo()
    


    uc.establish_connection()
    dted_array = geo.readAsArray()
    object = Object(dted_array)
    #plotify.plot_contour_map(dted_array)

    start = time.time()
    while True:
        end = time.time()
        unity_data = uc.receive_data()
        x,y,height = object.find_position(unity_data)
        #plotify.plot_object_position(x,y,dted_array)
        near_points = object.find_nearly_heights(height)


        if counter == 0:
            for i in range(0,len(near_points[0]),100):
                #particle oluştur 
                particles += [Particle(near_points[1][i],near_points[0][i],height)]
            

        else:
            for i in range(len(particles)):
                particles[i].move()

        plotify.live_plot(x,y,dted_array,particles,counter)

        print(f"{abs(end-start)}, counter : {counter}")
        counter += 1


        time.sleep(0.5)