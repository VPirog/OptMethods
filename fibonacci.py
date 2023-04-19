from init import *


def fibonacci( _a0=-a0, _b0=b0, eps=epsilon):
    n = 0
    for i in range(1000):
        delta_n = ((2 / (5 ** (1 / 2) + 1)) ** (i + 1)) * ((_b0 - _a0) * 5 ** (1 / 2))
        if delta_n <= eps:
            n = i
            break

    fib = lambda nn: (((1 + 5 ** (1 / 2)) / 2) ** nn - (((1 - 5 ** (1 / 2)) / 2) ** nn)) * 1 / 5 ** (1 / 2)
    a, b, epsn = [], [], []
    a.append(_a0)
    b.append(_b0)
    x1 = 0
    for i in range(n):
        x1 = a[i] + (_b0 - _a0) * (fib(n - i) / fib(n + 1))
        x2 = a[i] + (_b0 - _a0) * (fib(n - i + 1) / fib(n + 1))
        if func(x1) <= func(x2):
            a.append(a[i])
            b.append(x2)
        else:
            a.append(x1)
            b.append(b[i])
    print(n)
    return (x1)


