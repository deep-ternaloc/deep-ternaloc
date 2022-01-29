import matplotlib.pyplot as plt
import numpy as np
import time


def create_poles(poles, distance):
    y = np.zeros(distance)
    for p in poles:
        y[p] = 1
    x = range(distance)
    plt.stem(x, y, use_line_collection=True)


def plot_poles(poles, distance):
    plt.subplot(311)
    plt.yticks([])
    plt.xticks([])
    plt.xlim([-0.9, distance + 0.9])
    create_poles(poles, distance)


def plot_belief(y, distance):
    plt.subplot(312)
    plt.yticks([])
    plt.xlim([-0.9, distance + 0.9])
    plt.plot([0, distance], [0, 0], '-b')
    x = range(distance)
    for i in range(distance):
        plt.plot([i, i], [0, y[i]], '-b')


def plot_current_measurement(loc, poles, distance):
    plt.subplot(313)
    plt.yticks([])
    plt.xticks([])
    plt.xlim([loc - 1.5, loc + 1.5])
    plt.ylim([-0.1, 1.1])

    plt.plot([loc + 0.2], [0.6], 'g<', markersize=40)
    plt.plot([loc], [0.4], 'bo', markersize=40)
    create_poles(poles, distance)


def plot(distance, poles, P_loc_i_posterior, robot, block=False, pause_time=1):
    if robot.detect_pole(poles):
        block = True
    plot_poles(poles, distance)
    plot_belief(P_loc_i_posterior, distance)
    plot_current_measurement(robot.loc, poles, distance)
    if block:
        plt.show()
    else:
        plt.pause(0.1)
        plt.show(block=block)
        plt.pause(pause_time)
        plt.close()
