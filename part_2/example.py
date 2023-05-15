import numpy as np


def f(x):
    return 3 * x[0] ** 2 + 5 * x[1] ** 2 + 4 * x[2] ** 2 + 2 * x[0] * x[1] - x[0] * x[2] - x[1] * x[2] + 7 * x[0] + x[2]


def ff(x):
    return 10 * x[0] ** 2 + 3 * x[0] * x[1] + x[1] ** 2 + 10 * x[1]


def grad_f(x):
    return np.array([6 * x[0] + 2 * x[1] - x[2] + 7, 2 * x[0] + 10 * x[1] - x[2], -x[0] - x[1] + 8 * x[2] + 1])


def grad_ff(x):
    return np.array([20 * x[0] + 3 * x[1], 3 * x[0] + 2 * x[1] + 10])
