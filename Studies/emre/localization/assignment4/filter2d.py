from sim.plot2d import plot
import random as r
import math


class Position:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.theta = pos[2]


class Pole(Position):
    def __init__(self, pos):
        Position.__init__(self, pos)


class Measurement:
    def __init__(self, distance, angle):
        self.distance = distance
        self.angle = angle


class Robot(Position):
    def __init__(self, pos):
        Position.__init__(self, pos)
        self.measurements = []
        self.max_measurement = 200

    # Movement is perfectly accurate, even though we are assuming it isn't.
    def move(self, speed, theta_dot):
        ### START STUDENT CODE
        self.theta += 0
        self.x += 0
        self.y += 0
        ### END STUDENT CODE

    def move_with_error(self, speed, theta_dot):
        ### START STUDENT CODE
        self.move(speed, theta_dot)
        ### END STUDENT CODE

    # Measurement is perfectly accurate even though we are assuming it isn't.
    def measure(self, poles):
        ### START STUDENT CODE
        self.measurements = []
        ### END STUDENT CODE


class Particle(Robot):
    def __init__(self, pos):
        Robot.__init__(self, pos)
        self.weight = 0.0
        self.distance_sigma = 5
        self.distance_distribution_peak = 1 / \
            (math.sqrt(2 * math.pi) * self.distance_sigma)
        self.distance_weight = 1
        self.angle_sigma = 0.5
        self.angle_distribution_peak = 1 / \
            (math.sqrt(2 * math.pi) * self.angle_sigma)
        self.angle_weight = 1
        self.theta_dot_sigma = 0.2
        self.speed_sigma = 0.5

    def predict(self, speed, theta_dot):
        ### START STUDENT CODE
        return 0
        ### END STUDENT CODE

    def probability_density_function(self, mu, sigma, x):
        ### START STUDENT CODE
        return 0
        ### END STUDENT CODE

    def update_weight(self, robot_measurements):
        ### START STUDENT CODE
        self.weight = 0
        ### END STUDENT CODE


def resample_particles(particles):
    ### START STUDENT CODE
    resampled_particles = []
    return resampled_particles
    ### END STUDENT CODE
