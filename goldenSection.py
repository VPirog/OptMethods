from init import *


def goldenSection(eps=0.001, _a0=a0, _b0=b0):
    a, b, epsn = [], [], []
    a.append(_a0)
    b.append(_b0)
    delta = eps / 2

    for i in range(1000):
        x1 = a[i] + ((3 - 5 ** 0.5) / 2) * (b[i] - a[i])
        x2 = a[i] + ((5 ** 0.5 - 1) / 2) * (b[i] - a[i])
        if func(x1) <= func(x2):
            a.append(a[i])
            b.append(x2)
        else:
            a.append(x1)
            b.append(b[i])
        epsn.append(abs(b[i] - a[i]))
        if epsn[i] < eps:
            return ((a[i] + b[i]) / 2)


print(goldenSection())
