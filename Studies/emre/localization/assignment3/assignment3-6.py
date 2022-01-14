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

    # Movement is perfectly accurate, even though we are assuming it isn't.
    def move(self):

    # Measurement is perfectly accurate even though we are assuming it isn't.
    def measure(self, poles):


class Particle(Robot):
    def __init__(self, pos):

    def predict(self):

    def probability_density_function(self, mu, x):

    def update_weight(self, robot_dist):


def resample_particles(particles):
    # Potentially resample uniformly if weights are so low.
    return resampled_particles



def initialize_particles(particles):


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
