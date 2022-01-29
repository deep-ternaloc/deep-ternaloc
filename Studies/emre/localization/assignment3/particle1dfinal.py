import matplotlib.pyplot as plt
import numpy as np
import random as r
import math
from sim.plot import plot, print_particle_error


AUTORUN = False
robot_start = 7
num_particles = 20
distance = 40
poles = [10, 15, 17, 19, 30, 39]


### START STUDENT CODE
class Robot:
    def __init__(self, pos):

        self.pole_dist = 0
        self.pos = pos
        self.move_dist = 2
        self.max_measurement = 3


    # Movement is perfectly accurate, even though we are assuming it isn't.
    def move(self):
        self.pos += self.move_dist


    # Measurement is perfectly accurate even though we are assuming it isn't.
    def measure(self, poles):
        for pole in poles:
            if pole-self.pos <= self.max_measurement and pole-self.pos > 0:
                self.pole_dist = pole-self.pos
                break
            else:
                self.pole_dist = -100



class Particle(Robot):
    def __init__(self, pos):
        Robot.__init__(self, pos)
        self.weight = 0
        self.measurement_sigma = 0.2
        self.movement_sigma =  0.2

    def predict(self):
        self.pos += np.random.normal(self.move_dist, self.movement_sigma)

    def probability_density_function(self, mu, x):
        sigma = self.measurement_sigma

        return 1/(sigma*math.sqrt(2*math.pi))*math.e**(-0.5 * ((x-mu)/sigma)**2)

    def update_weight(self, robot_dist):

        self.weight = self.probability_density_function(robot_dist, self.pole_dist)



def resample_particles(particles):
    # Potentially resample uniformly if weights are so low.
    weights = []

    for particle in particles:
        weights += [particle.weight]

    if (sum(weights)<0.05):
        resampled_particles=[]
        for i in range(len(particles)):
            resampled_particles += [Particle(r.uniform(0,39))]
        return resampled_particles


    resample = r.choices(range(len(particles)), weights=weights, k=len(particles))
    print(resample)
    print(weights)


    resampled_particles = []

    for i in resample:
        resampled_particles += [Particle(particles[i].pos)]
        print(particles[i].pos)
    return resampled_particles
    
    
    



def initialize_particles(particles):
    for i in range(0,num_particles,1):
        particles.append(Particle(i))
        
    


### END STUDENT CODE

robot = Robot(robot_start)

# Setup particles.
particles = []
initialize_particles(particles)

# Plot starting distribution, no beliefs
plot(particles, poles, robot.pos)

# Begin Calculating
for j in range(39 - robot.pos):
    # Move
    if j != 0:
        robot.move()
        for particle in particles:
            particle.predict()

    # Measure
    robot.measure(poles)
    for particle in particles:
        particle.measure(poles)

        # Update Beliefs
        particle.update_weight(robot.pole_dist)

    print_particle_error(robot, particles)

    # Resample
    resampled_particles = resample_particles(particles)
    plot(particles, poles, robot.pos, resampled_particles, j, AUTORUN)
    particles = resampled_particles

plot(particles, poles, robot.pos, resampled_particles)
