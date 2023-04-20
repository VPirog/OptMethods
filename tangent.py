from init import *


def tangent(_a0=a0, _b0=b0, eps=epsilon):
    a, b, x = [], [], []
    a.append(_a0)
    b.append(_b0)
    a.append(_a0)
    b.append(_b0)
    x.append(_a0)
    x.append(_b0)

    for i in range(1, 1000):
        tmp1 = (b[i] * dif_func(b[i]) - a[i] * dif_func(a[i]) + func(a[i]) - func(b[i]))
        tmp2 = (dif_func(b[i]) - dif_func(a[i]))
        x.append(tmp1 / tmp2)

        tmp4 = dif_func(x[i + 1])
        if tmp4 >= 0:
            a.append(a[i])
            b.append(x[i + 1])
        if tmp4 < 0:
            a.append(x[i + 1])
            b.append(b[i])
        pass
        tmp3 = abs(dif_func(x[i + 1]))
        # print(x, a, b, dif_func(x[i + 1]))
        if tmp3 <= eps:
            print(i)
            return x[i + 1]
    return x.pop()
