from helpers import plot_poles, plot_measurement_circles, plot_robot
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def distance_difference_squared(guess_location, pole, pole_measurement):
    ### STUDENT CODE START
    output = 0
    # calc distance between guess location and pole.
    # compare distance vs pole_measurement
    output = np.sqrt((guess_location[0] - pole[0])**2 + (guess_location[1] - pole[1])**2) - pole_measurement
    ### STUDENT CODE END
    return output**2

def total_cost(guess_location, poles, pole_measurements):
    total = 0
    total += distance_difference_squared(guess_location, poles[0], pole_measurements[0])
    total += distance_difference_squared(guess_location, poles[1], pole_measurements[1])
    total += distance_difference_squared(guess_location, poles[2], pole_measurements[2])
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
plot_measurement_circles(poles, pole_measurements)
plt.title('Pole Measurements')
plt.show()

location_solution = minimize(total_cost, [0, 0], method='Nelder-Mead', args=(poles, pole_measurements))
print(location_solution)

plot_poles(poles)
plot_measurement_circles(poles, pole_measurements)
plot_robot(location_solution.x)
plt.title('Calculated Location')
plt.show()
