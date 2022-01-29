import matplotlib.pyplot as plt
import math


def plot_particles(particles, distance, show=True):
    plt.xlim([-0.9, distance + 0.9])
    for particle in particles:
        plt.plot([particle.pos], [0.0], '*', color=particle.color)
    if show:
        plt.show()


def plot_resample_counts(particles, resample, i_count, distance, show=True):
    plot_particles(particles, distance, show=False)
    for i in range(len(particles)):
        i_count += [resample.count(i)]
        plt.plot([particles[i].pos, particles[i].pos],
                 [0.0, -i_count[-1]], 'g-')
    if show:
        plt.show()


def plot_resampled(
        particles,
        resample,
        i_count,
        resampled_particles,
        distance,
        show=True,
        move=False):
    plot_particles(particles, distance, show=False)
    plot_resample_counts(particles, resample, i_count, distance, show=False)
    for particle in resampled_particles:
        if move:
            particle.predict()
        plt.plot([particle.pos], [-max(i_count)], '*', color=particle.color)
    if show:
        plt.show()


def plot(particles, resampled_particles, resample, distance):
    i_count = []
    # Plot 1
    plot_particles(particles, distance)
    # Plot 2
    plot_resample_counts(particles, resample, i_count, distance)
    # Plot 3
    plot_resampled(particles, resample, i_count, resampled_particles, distance)
    # Plot 4
    plot_resampled(
        particles,
        resample,
        i_count,
        resampled_particles,
        distance,
        move=True)
