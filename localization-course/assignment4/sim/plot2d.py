import matplotlib.pyplot as plt
import math

distance = 100


def draw_robot(robot, error):
    line_length = 2
    o = math.sin(robot.theta) * line_length + robot.y
    a = math.cos(robot.theta) * line_length + robot.x
    if error:
        plt.plot([robot.x], [robot.y], 'ro', markersize=6)
    else:
        plt.plot([robot.x], [robot.y], 'ro', markersize=10)
    plt.plot([robot.x, a], [robot.y, o], 'r-', linewidth=4)


def draw_particles(particles, error):
    for particle in particles:
        line_length = 2
        o = math.sin(particle.theta) * line_length + particle.y
        a = math.cos(particle.theta) * line_length + particle.x
        if error:
            plt.plot([particle.x], [particle.y], 'bo', markersize=6)
        else:
            plt.plot([particle.x], [particle.y], 'bo', markersize=10)
        plt.plot([particle.x, a], [particle.y, o], 'b-', linewidth=4)


def draw_poles(poles):
    for pole in poles:
        plt.plot([pole.x], [pole.y], 'gs', markersize=15)


def plot(
        robot,
        particles=None,
        poles=None,
        j=None,
        autorun=False,
        time=1,
        error=False):
    plt.figure(figsize=[8, 8])
    if j is not None:
        plt.title(str(j))
    plt.grid(linestyle='--')
    plt.yticks([0, int(distance / 4), int(distance / 2),
                int(distance * 3 / 4), distance])
    plt.xticks([0, int(distance / 4), int(distance / 2),
                int(distance * 3 / 4), distance])
    if particles is not None:
        draw_particles(particles, error)
    if poles is not None:
        draw_poles(poles)
    draw_robot(robot, error)
    plt.xlim([0, distance])
    plt.ylim([0, distance])
    if error:
        plt.xlim([-distance * 0.2, distance * 1.2])
        plt.ylim([-distance * 0.2, distance * 1.2])

    if autorun:
        if j == 0:
            # Not sure why this is needed but it is.
            plt.pause(time)
        plt.show(block=False)
        plt.pause(time)
        plt.close()
    else:
        plt.show()


def print_particle_error(robot, particles):
    weights = []
    for particle in particles:
        weights += [particle.weight]
    best_particle = weights.index(max(weights))
    diff_x = round(abs(robot.x - particles[best_particle].x), 1)
    diff_y = round(abs(robot.y - particles[best_particle].y), 1)
    diff_pos = round(diff_x + diff_y, 2)
    diff_theta = round(abs(robot.theta - particles[best_particle].theta), 2)
    if diff_theta > math.pi:
        diff_theta = round(abs(diff_theta - math.pi * 2), 2)
    print("Error: [" + str(diff_pos) + ", " + str(diff_theta) + "]")
    print("Weight Sum: " + str(round(sum(weights), 2)))
    print("Max Weight: " + str(round(particles[best_particle].weight, 2)))
    if (diff_pos < 3) and (diff_theta < 0.5):
        print("Converged!")
