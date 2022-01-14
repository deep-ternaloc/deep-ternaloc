from sim.plot2d import plot, print_particle_error
from filter2d import Robot, Particle, Pole, resample_particles
import random as r
import math


# r.seed(939)
robot = Robot([10, 10, 0])
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


moves = []
for i in range(60):
    if i < 10:
        moves += [[5, 0]]
        continue
    if i < 20:
        moves += [[5, math.pi / 10]]
        continue
    if i < 30:
        moves += [[-3, -math.pi / 20]]
        continue
    if i < 35:
        moves += [[10, 0]]
        continue
    if i < 45:
        moves += [[2, -math.pi / 5]]
        continue
    if i < 55:
        moves += [[4, math.pi / 20]]
        continue

    moves += [[0, 0]]

for i in range(60):
    # Move Robot
    robot.move_with_error(moves[i][0], moves[i][1])  # add noise here
    robot.measure(poles)                 # and add noise here
    # Move and Update Particles
    for particle in particles:
        particle.predict(moves[i][0], moves[i][1])
        particle.measure(poles)
        particle.update_weight(robot.measurements)
    # Resample
    print_particle_error(robot, particles)
    particles = resample_particles(particles)
    plot(robot, particles, poles, j=i, autorun=True, time=0.5, error=True)
plot(robot, particles, poles, error=True)
