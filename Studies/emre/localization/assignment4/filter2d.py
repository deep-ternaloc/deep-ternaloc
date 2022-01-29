

from numpy import angle
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
        self.theta += theta_dot

        print(self.theta)
        self.x += speed * math.cos(self.theta)
        self.y += speed * math.sin(self.theta)
        ### END STUDENT CODE

    def move_with_error(self, speed, theta_dot):
        ### START STUDENT CODE
        self.move(speed, theta_dot)
        ### END STUDENT CODE

    # Measurement is perfectly accurate even though we are assuming it isn't.
    def measure(self, poles):
        ### START STUDENT CODE
        self.measurements = []

        for pole in poles:
            x_diff = pole.x - self.x
            y_diff = pole.y - self.y
            distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
            angle = math.atan2(y_diff, x_diff)

            self.measurements += [Measurement(distance, angle)]

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
        
        theta_dot = r.normalvariate(theta_dot, self.theta_dot_sigma)
        speed = r.normalvariate(speed, self.speed_sigma)
        self.move(speed, theta_dot)

        ### END STUDENT CODE

    def probability_density_function(self, mu, sigma, x):
        ### START STUDENT CODE
        return 1/(sigma*math.sqrt(2*math.pi))*math.e**(-0.5 * ((x-mu)/sigma)**2)
        ### END STUDENT CODE

    def update_weight(self, robot_measurements):
        ### START STUDENT CODE
        for p in self.measurements:
            best_match = 0
            for r in robot_measurements:
                distance_match = self.probability_density_function(r.distance, self.distance_sigma, p.distance)

                distance_match = distance_match / self.distance_distribution_peak
                distance_match *=self.distance_weight



                diff_angle = abs(p.angle - r.angle)
                if diff_angle > math.pi:
                    diff_angle= abs(diff_angle - 2*math.pi)

                angle_macth = self.probability_density_function(0, self.angle_sigma, diff_angle)

                angle_macth *=self.angle_weight

                match = angle_macth * distance_match

                if match > best_match:
                    best_match = match
            self.weight += best_match
        if len(robot_measurements) == 0:
            return
        self.weight /= len(robot_measurements)
        self.weight *= self.weight

            

def resample_particles(particles):
    ### START STUDENT CODE
    weights = []

    for particle in particles:
        weights += [particle.weight]

    scale = len(particles) / (sum(weights)*5)


    if scale > 10:
        scale =  10

    resample = r.choices(range(len(particles)), weights, k=len(particles))

    resampled_particles = []
    
    for i in resample:
        x= particles[i].x +r.normalvariate(0,particles[0].speed_sigma*scale)

        y= particles[i].y +r.normalvariate(0,particles[0].speed_sigma*scale)

        theta = particles[i].theta +r.normalvariate(0,particles[0].theta_dot_sigma*scale)

        resampled_particles += [Particle([x,y,theta])]

    return resampled_particles

    
    
    return resampled_particles
    ### END STUDENT CODE
