import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.axes as axes

def plot_poles(poles):
    for pole in poles:
        plt.plot(pole[0], pole[1], 'ob')
    plt.ylim(-1, 11)
    plt.xlim(-1, 11)

def plot_robot(robot_loc):
    plt.plot(robot_loc[0], robot_loc[1], 'g^')

def plot_measurements(robot_loc, poles):
    for pole in poles:
        plt.plot([robot_loc[0],pole[0]], [robot_loc[1], pole[1]], '-r')
    plot_robot(robot_loc)

def plot_measurement_circles(poles, pole_measurements):
    ax = plt.gca()
    for i in range(len(poles)):
        c = patches.Circle(poles[i], pole_measurements[i], color='r', fill=False, lw=4)
        ax.add_patch(c)

def plot_measurement_circles2(poles, pole_measurements, zoom_out=False):
    ax = plt.gca()
    for pole in poles:
        c = patches.Circle(pole, pole_measurements[0], color='r', fill=False, lw=4)
        ax.add_patch(c)
        c = patches.Circle(pole, pole_measurements[1], color='m', fill=False, lw=4)
        ax.add_patch(c)
        c = patches.Circle(pole, pole_measurements[2], color='y', fill=False, lw=4)
        ax.add_patch(c)

    if zoom_out:
        plt.ylim(-20, 30)
        plt.xlim(-20, 30)
