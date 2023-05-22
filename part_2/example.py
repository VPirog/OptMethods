import numpy as np


def f(x):
    return 3 * x[0] ** 2 + 4 * x[1] ** 2 + 5 * x[2] ** 2 + 2 * x[0] * x[1] - x[0] * x[2] - 2 * x[1] * x[2] + x[0] - 3 * x[2]


def ff(x):
    return 3 * x[0] ** 2 - 3 * x[0] * x[1] + 4 * x[1] ** 2 - 2 * x[0] + x[1]


def grad_f(x):
    return np.array([6 * x[0] + 2 * x[1] - x[2] + 1, 2 * x[0] + 8 * x[1] - 2 * x[2], -x[0] - 2 * x[1] + 10 * x[2] - 3])


def grad_ff(x):
    return np.array([6 * x[0] - 3 * x[1] - 2, -3 * x[0] + 8 * x[1] + 1])
