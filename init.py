from numpy import sin, pi, cos, linspace

epsilon = 10 ** (-8)

print("------Выберите функцию------")
print("1 === x ** 2 - sin(x)")
print("2 === x * cos(2 * x) + 1")

choose = (input())
# choose = 1

match choose:
    case '1':
        def func(x):
            return x ** 2 - sin(x)


        a0 = 0
        b0 = pi / 2


        def dif_func(x):
            return 2 * x - cos(x)


        def sec_dif_func(x):
            return 2 + sin(x)

    case '2':
        def func(x):
            return x * cos(2 * x) + 1


        def dif_func(x):
            return cos(2 * x) - 2 * sin(2 * x) * x


        def sec_dif_func(x):
            return -4 * sin(2 * x) - 4 * cos(2 * x) * x


        a0 = -1
        b0 = 6
    case 'test':

        def func(x):
            return (x + 1) ** 2


        def dif_func(x):
            return (x + 1) * 2


        def sec_dif_func(x):
            return 2


        a0 = -10
        b0 = 6
    case _:
        raise Exception('ГГ')

LL = - 10 ** 10

for j in linspace(a0, b0, 10000):
    if LL < dif_func(j):
        LL = dif_func(j)

LL = int(LL) + 1
