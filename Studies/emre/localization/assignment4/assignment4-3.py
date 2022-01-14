from sim.plot2d import plot
from filter2d import Robot, Particle, Pole
import random as r
import math

robot = Robot([50, 50, 0])
poles = [Pole([25, 25, 0])]
# Probably comment for real assignment.
poles += [Pole([25, 50, 0])]
particles = []
particles += [Particle([50, 50, 0])]
particles += [Particle([50, 50, math.pi / 8])]
particles += [Particle([75, 75, 0])]
particles += [Particle([55, 55, -math.pi / 4])]
particles += [Particle([45, 35, 0])]

robot.measure(poles)
for particle in particles:
    particle.measure(poles)
    particle.update_weight(robot.measurements)
    print("Weight: " + str(round(particle.weight, 2)))
    for measure in particle.measurements:
        print("Measurements: " + str(round(measure.distance, 2)))

print()
print("Answers:")
print("Weight: 1.0")
print("Weight: 0.54")
print("Weight: 0.0")
print("Weight: 0.12")
print("Weight: 0.25")
plot(robot, particles, poles)
