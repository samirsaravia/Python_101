from random import choice
import matplotlib.pyplot as plt


def rand_walk(num):
    """
        Setting a list up
    :param num:digit which is the length of the list that'll be created
    :return: a defined length list with its random digits
    """

    direction = [1, -1]
    walk = [choice(direction)]
    for step in range(1, num + 1):
        step_2 = walk[step - 1] + choice(direction)
        walk.append(step_2)
    return walk


def show_plot(steps):
    """
        Data visualization
    :param steps: a list of int digits
    display a third party graphic data
    """

    x = list(range(1, len(steps) + 1))
    plt.plot(x, steps)
    plt.xlim(0, len(x) + 1)
    plt.title('Walk Random')
    plt.xlabel('Number of steps')
    plt.ylabel('Distance from origin')
    plt.show()


show_plot(rand_walk(100))
