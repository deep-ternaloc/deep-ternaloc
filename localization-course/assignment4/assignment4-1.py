from sim.plot2d import plot
from filter2d import Robot, Particle
import random as r
import math

robot = Robot([50, 50, 0])
particles = []
for i in range(100):
    particles += [Particle([50, 50, 0])]
plot(robot, particles)

autorun = True
for j in range(10):
    robot.move(5, math.pi * 2 / 10)
    for particle in particles:
        particle.predict(5, math.pi * 2 / 10)
    plot(robot, particles, j=j, autorun=autorun)

plot(robot, particles)
