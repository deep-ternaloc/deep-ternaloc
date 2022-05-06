
import numpy as np
import math
import random as r
from objectify.object import Object

scale = 108000/3600




class Position():
    def __init__(self,x,y,h):
        '''
        :param x: x position
        :param y: y position
        :param h: height from sea level

        '''
        self.x = x
        self.y = y
        self.height = h


class Plane():
    def __init__(self,x,y,h):
        Position.__init__(self,x,y,h)

        self.measurements = []

    def move(self,theta_dot):
        '''
        :param theta_dot: angular velocity, enter 0 for moving straight

        '''
        self.x += theta_dot * math.cos(self.theta)
        self.y += theta_dot * math.sin(self.theta)


    def measure(self):
        '''
        We don't have multiple measurements, so we just pass this

        '''
        pass

    

class Particle():
    def __init__(self,x,y,h):
        Position.__init__(self,x,y,h)
        self.measurements = []
        self.weight = 0
        self.theta = 0
        self.interval = 0
        self.speed = 30
        self.scale = scale
        self.x_list = []
        self.y_list = []
        self.x_list.append(x)
        self.y_list.append(y)
        self.measurement_sigma = 3
        self.sum_prob = 0
        self.movement_sigma = 30
    def move(self,speed):
        '''
        :param theta_dot: angular velocity, enter 0 for moving straight

        '''
        #print(f"Hiz {speed}")
        #print(f"Mov. Sigma  {np.random.normal(speed, self.movement_sigma)}")
        self.y += np.random.normal(speed, self.movement_sigma) #* math.cos(self.theta)
        self.x += (self.speed/scale) * math.sin(self.theta)

         
        self.x_list.append(self.x)
        self.y_list.append(self.y)


    def measure_height(self, data):
        '''

        :param scale: scale of the map
        :param data: dted
        :param interval: interval for height data to accept
        :param speed: speed of the plane
        '''
        self.height = data[int(self.y),int(self.x)]


        #place particle next position on matplotlib


    def probability_density_function(self, mu, x):
        sigma = self.measurement_sigma

        #print(f"e'li ifade {1/(sigma*math.sqrt(2*math.pi))*math.e**(-0.5 * (((x-mu))/sigma)**2)}")
        #print(f"e'nin solu {1/(sigma*math.sqrt(2*math.pi))}")
        
        return 1/(sigma*math.sqrt(2*math.pi))*math.e**(-0.5 * ((x-mu)/sigma)**2)
    

    def normalize(weights):
        return (weights-np.min(weights)) / (np.max(weights)-np.min(weights))

    def update_weight(self, robot_height,counter):
        #print(self.x, self.y)


            #print(self.weight)
        weight = self.probability_density_function(robot_height, self.height)

        if counter%5 != 0:

            self.weight += weight 
        
        else:

            self.weight = self.probability_density_function(robot_height,self.height)
        

        self.sum_prob += self.weight


    
    def resample_particles(particles,dted_array):
        weights = []

        for particle in particles:
            weights += [particle.weight]

        weights = Particle.normalize(weights)
        print("Toplam Weight: {}, Particle sayisi {} ".format(sum(weights), len(particles)))

        

        if (sum(weights)<0.05):
            resampled_particles = []
            
                #particle oluştur 
                

            try:
                for i in range (1000):
                    x_particle = r.randint(0,3600)
                    y_particle = r.randint(0,3600)
                    height = dted_array[y_particle][x_particle]
                    resampled_particles += [Particle(x_particle,y_particle,height)]
            except:
                pass

            print("low weight ! ! !")
            return resampled_particles

        #    resampled_particles=[]
        #    xy_min = np.min(np.min(near_points,axis=1),axis=0)
        #    xy_max = np.max(np.max(near_points,axis=1),axis=0)
        #    for i in range(len(particles)):
        #        resampled_particles += [Particle(r.uniform(low=xy_min,high=xy_max,size=(len(particles))))]
        #    return resampled_particles
    
        
        print(f"Normalized weight sum: {sum(weights)}")
        print(f"Max weight: {max(weights)}")
        print(f"Min weight: {min(weights)}")
        resample = r.choices(range(len(particles)), weights=weights, k=len(particles))
        


        #print("Resampled: {}".format(len(resample)))
        #print(resample)
        #print(weights)
    
    
        resampled_particles = []

        for i in resample:
            
            resampled_particles += [Particle(particles[i].x,particles[i].y,particles[i].height)]

        print("Resampled: {}".format(len(resampled_particles)))

        return resampled_particles




    def print_particle_error(height, particles):
        weights = []
        for particle in particles:
            weights += [particle.weight]
        best_particle = weights.index(max(weights))
        print("Error: " +
              str(round(abs(particles[best_particle].height - height), 2)))

        print("Weight Sum: " + str(sum(weights)))
        print()


    def pdf_control(particles):
        sum_probability = 0
        for particle in range(int(len(particles)/2)):
            sum_probability += particles[particle].weight
        
        print(f"PDF (if close to 0.5 it works) {round(sum_probability*0.01,2)}")
