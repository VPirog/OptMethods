from numpy import sin, pi, cos, linspace

epsilon = 10 ** (-10)


# def func(x):
#     return x ** 2 - sin(x)
#
#
# a0 = 0
# b0 = pi / 2


def func(x):
    return x * cos(2 * x) + 1


def dif_func(x):
    return cos(2 * x) - 2 * sin(2 * x) * x


a0 = -1
b0 = 6
LL = - 10 ** 10

for i in linspace(a0, b0, 10000):
    if LL < dif_func(i):
        LL = dif_func(i)

LL = int(LL) + 1
