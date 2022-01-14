import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

distance = 40


def create_poles(poles):
    y = np.zeros(distance)
    for p in poles:
        y[p] = 1
    x = range(distance)
    plt.stem(x, y, use_line_collection=True)


def plot_robot_measurement(poles, pos, gs):
    plt.subplot(gs[2:3, 0])
    plt.yticks([])
    plt.xticks([])
    plt.xlim([pos - 1.5, pos + 3.5])
    plt.ylim([-0.1, 1.1])
    plt.plot([pos + 0.2], [0.6], 'g<', markersize=40)
    plt.plot([pos], [0.4], 'bo', markersize=40)
    create_poles(poles)


def plot_simple(particles, poles, pos=None, j=None):
    gs = gridspec.GridSpec(3, 1)
    # Plot Main Display
    plt.subplot(gs[0:2, 0])
    if j is not None:
        plt.title(str(j))
    plt.yticks([])
    plt.xlim([-0.9, distance + 0.9])
    for particle in particles:
        if particle.belief == 0:
            continue
        plt.plot([particle.pos], [0.5], '*', color=particle.color)
    create_poles(poles)

    # Plot Robot Measurement
    if pos is not None:
        plot_robot_measurement(poles, pos, gs)
    plt.show(block=True)


def plot(
        particles,
        poles,
        pos,
        resampled_particles=None,
        j=None,
        autorun=False):
    gs = gridspec.GridSpec(3, 1)
    # Plot Main Display
    plt.subplot(gs[0:2, 0])
    if j is not None:
        plt.title(str(j))
    plt.yticks([])
    plt.xlim([-0.9, distance + 0.9])
    for particle in particles:
        plt.plot([particle.pos], [0.5], 'b*', label="Particles")
    if resampled_particles is not None:
        for particle in resampled_particles:
            plt.plot([particle.pos], [0.25], 'g*', label="Resampled")
    plt.plot([pos], [0.65], 'r*', label="Robot")
    # Remove duplicates in legend (because of way I plotted one at a time.
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc='upper right')

    create_poles(poles)

    # Plot Robot Measurement
    if pos is not None:
        plot_robot_measurement(poles, pos, gs)
    if autorun:
        if j == 0:
            # Not sure why this is needed but it is.
            plt.pause(1)
        plt.show(block=False)
        plt.pause(1)
        plt.close()
    else:
        plt.show()

def print_particle_error(robot, particles):
    weights = []
    for particle in particles:
        weights += [particle.weight]
    best_particle = weights.index(max(weights))
    print("Error: " +
          str(round(abs(particles[best_particle].pos - robot.pos), 2)))
    print("Weight Sum: " + str(sum(weights)))
    print()
