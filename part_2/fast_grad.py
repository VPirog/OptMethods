import numpy as np
from part_1 import golden_section


def f(x):
    return 3 * x[0] ** 2 + 5 * x[1] ** 2 + 4 * x[2] ** 2 + 2 * x[0] * x[1] - x[0] * x[2] - x[1] * x[2] + 7 * x[0] + x[2]


def grad_f(x):
    return np.array([6 * x[0] + 2 * x[1] - x[2] + 7, 2 * x[0] + 10 * x[1] - x[2], -x[0] - x[1] + 8 * x[2] + 1])


def f_alpha(x, alpha):
    return f(x - alpha * grad_f(x))


alpha_min = 0.0001
alpha_max = 1.0


def gradient_descent(x0, eps):
    x = x0
    i = 0
    while True:
        f_alpha = lambda alpha: f(x - alpha * grad_f(x))
        alpha = golden_section(f_alpha, alpha_max, alpha_min)
        x_new = x - alpha * grad_f(x)
        if np.linalg.norm(x_new - x) < eps:
            print(i)
            return x_new
        x = x_new
        i += 1


def gradient(x0, eps):
    x = x0
    alpha_prev = 0
    i = 0
    while True:
        alpha = alpha_min
        while f(x - alpha * grad_f(x)) >= f(x) and alpha >= 1e-8:
            alpha /= 2
        if alpha < 1e-8:
            break
        x_new = x - alpha * grad_f(x)
        if np.linalg.norm(x_new - x) < eps:
            print(i)
            return x_new
        if f(x_new) >= f(x):
            alpha = alpha_prev / 2
            x_new = x - alpha * grad_f(x)
            if np.linalg.norm(x_new - x) < eps:
                print(i)
                return x_new
        alpha_prev = alpha
        x = x_new
        i += 1


x_list = [np.array([1, 2, 3])]
a = 0.001
eps = 10 ** (-5)
print(f(gradient_descent(np.array([1, 2, 3]), eps)))

print(f(gradient(np.array([1, 2, 3]), eps)))
