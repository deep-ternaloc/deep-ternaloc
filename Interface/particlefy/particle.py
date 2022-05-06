import numpy as np
import math

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

    def move(self,speed):
        '''
        :param theta_dot: angular velocity, enter 0 for moving straight

        '''
        self.y += (speed) * math.cos(self.theta)
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
        pass

        #place particle next position on matplotlib

    



    





