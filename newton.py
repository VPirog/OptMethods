from init import *


def newton(_a0=a0, _b0=b0, eps=epsilon):
    x0 = _a0 + _b0 / 2
    x = [x0]
    for i in range(1000):
        x.append(x[i] - (dif_func(x[i]) / sec_dif_func(x[i])))
        if abs(x[i + 1] - x[i]) < eps:
            print(i)
            return x[i + 1]
    return x.pop()
