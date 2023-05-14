import numpy as np
from scipy.optimize import approx_fprime


def f(x):
    return 3 * x[0] ** 2 + 5 * x[1] ** 2 + 4 * x[2] ** 2 + 2 * x[0] * x[1] - x[0] * x[2] - x[1] * x[2] + 7 * x[0] + x[2]


x_list = [np.array([1, 2, 3])]
a = 0.001
eps = 10 ** (-5)
x_list.append(x_list[0] - approx_fprime(x_list[0], f))

for i in range(1, 10000):
    if f(x_list[i]) > f(x_list[i - 1]):
        a /= 2
    tmp = approx_fprime(x_list[i], f)
    # print(i, np.linalg.norm(tmp), x_list[i])
    if np.linalg.norm(tmp) < eps:
        print(i)
        break
    x_list.append(x_list[i] - a * tmp)

print(x_list[-1], f(x_list[-1]))
