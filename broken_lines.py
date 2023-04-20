from init import *


def broken_lines(_a0=a0, _b0=b0, eps=epsilon, L = LL):
    x_opt = 1 / (2 * L) * (func(_a0) - func(_b0) + L * (_a0 + _b0))
    p = 1 / 2 * (func(_a0) + func(_b0) + L * (_a0 - _b0))

    for i in range(1000):
        delta = 1 / (2 * L) * (func(x_opt) - p)

        if (2 * L * delta) <= eps:
            print(i)
            return x_opt

        x1 = x_opt - delta
        x2 = x_opt + delta

        if func(x1) < func(x2):
            x_opt = x1
        else:
            x_opt = x2

        p = (1 / 2) * (func(x_opt) + p)




# open '/home/jorge/Изображения/Снимки экрана/Снимок экрана от 2023-04-19 18-21-07.png'
