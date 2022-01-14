from sim.plot2d import plot
from filter2d import Robot, Particle, Pole
import random as r
import math


robot = Robot([50, 50, 0])
poles = [Pole([90, 90, 0]), Pole([80, 50, 0]),
         Pole([50, 70, 0]), Pole([25, 50, 0])]


print("Robot Measurements:")
robot.measure(poles)
for measurement in robot.measurements:
    print("Distance: " + str(round(measurement.distance, 1)) +
          " Angle: " + str(round(measurement.angle, 2)))

print()
print("Measurement Answers:")
print("Distance: 56.6 Angle: 0.79")
print("Distance: 30.0 Angle: 0.0")
print("Distance: 20.0 Angle: 1.57")
print("Distance: 25.0 Angle: 3.14")
plot(robot, poles=poles)
