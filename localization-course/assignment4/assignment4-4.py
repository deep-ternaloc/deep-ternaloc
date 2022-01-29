from sim.plot2d import plot, print_particle_error
from filter2d import Robot, Particle, Pole, resample_particles
import random as r
import math


r.seed(939)
robot = Robot([50, 50, 0])
poles = []
num_poles = 5
for i in range(num_poles):
    x = r.uniform(0, 100)
    y = r.uniform(0, 100)
    poles += [Pole([x, y, 0])]
particles = []
num_particles = 100
for i in range(num_particles):
    x = r.uniform(0, 100)
    y = r.uniform(0, 100)
    theta = r.uniform(0, math.pi * 2)
    particles += [Particle([x, y, theta])]

plot(robot, particles, poles)

robot.measure(poles)
for i in range(20):
    for particle in particles:
        particle.measure(poles)
        particle.update_weight(robot.measurements)
    print_particle_error(robot, particles)
    particles = resample_particles(particles)
    plot(robot, particles, poles, j=i, autorun=True)
