from helpers import plot_poles, plot_measurement_circles2, plot_robot
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import random

def distance_difference_squared(guess_location, pole, pole_measurements):
    ### STUDENT CODE START
    output = 0
    output_list = []
    output = np.sqrt((guess_location[0] - pole[0])**2 + (guess_location[1] - pole[1])**2)
    for i in range(len(pole_measurements)):
        #print(str(output), str(pole_measurements[i])+"\n")

        output_list.append((output - pole_measurements[i])**2)

    output = random.randint(0,2)
    return output_list[output]
    

# 1D Example
# pole = 5
# pole_measurement = [3, 2, 7]
# guess_location = 3
# distance = 2


def total_cost(guess_location, poles, pole_measurements):
    total = 0
    total += distance_difference_squared(guess_location, poles[0], pole_measurements)
    total += distance_difference_squared(guess_location, poles[1], pole_measurements)
    total += distance_difference_squared(guess_location, poles[2], pole_measurements)
    return total

poles = [[0, 0]]
poles += [[3, 2]]
poles += [[7, 4]]
pole_measurements = [11.180339887498949]
pole_measurements += [7.615773105863909]
pole_measurements += [3.1622776601683795]

plot_poles(poles)
plt.title('Pole Location')
plt.show()

plot_poles(poles)
plot_measurement_circles2(poles, pole_measurements)
plt.title('Pole Measurements')
plt.show()

plot_poles(poles)
plot_measurement_circles2(poles, pole_measurements, zoom_out=True)
plt.title('Pole Measurements')
plt.show()

location_solution = minimize(total_cost, [0, 0], bounds=[[-20, 20], [-20, 20]], args=(poles, pole_measurements))
print(location_solution)

plot_poles(poles)
plot_measurement_circles2(poles, pole_measurements)
plot_robot(location_solution.x)
plt.title('Calculated Location')
plt.show()
