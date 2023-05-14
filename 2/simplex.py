import numpy as np


def rosenbrock(x):
    """Функция Розенброка"""
    return np.sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)


def f(x):
    return 10 * x[0] ** 2 + 3 * x[0] * x[1] + x[1] ** 2 + 10 * x[1]


def ff(x):
    return 3 * x[0] ** 2 + 5 * x[1] ** 2 + 4 * x[2] ** 2 + 2 * x[0] * x[1] - x[0] * x[2] - x[1] * x[2] + 7 * x[0] + x[2]


def hooke_jeeves(func, x0, delta=0.5, eps=1e-6, max_iter=1000):
    """
    Метод Хука-Дживса для оптимизации целевой функции

    :param func: целевая функция
    :param x0: начальная точка
    :param delta: шаг поиска
    :param eps: допустимое отклонение от оптимального решения
    :param max_iter: максимальное число итераций
    :return: найденное оптимальное решение
    """
    x1 = np.array(x0)
    x2 = np.array(x0)
    n = len(x0)
    for i in range(max_iter):
        for j in range(n):
            x2[j] = x1[j]
        for j in range(n):
            x1[j] = x2[j]
            f1 = func(x1)
            x1[j] = x2[j] + delta
            f2 = func(x1)
            if f2 < f1:
                while True:
                    delta *= 2.0
                    x3 = x2 + delta * (x2 - x0)
                    f3 = func(x3)
                    if f3 < f2:
                        x1 = x3
                        f1 = f3
                        x2 = x3 - delta * (x3 - x2)
                        f2 = func(x2)
                    else:
                        break
                x2 = x1 + delta * (x1 - x2)
                x1 = x3
            else:
                x1[j] = x2[j] - delta
                f3 = func(x1)
                if f3 < f1:
                    while True:
                        delta *= 2.0
                        x3 = x2 + delta * (x2 - x0)
                        f3 = func(x3)
                        if f3 < f2:
                            x2 = x1
                            x1 = x3
                            f2 = f1
                            f1 = f3
                            x2 = x3 - delta * (x3 - x1)
                        else:
                            break
                    x2 = x1 + delta * (x1 - x2)
                    x1 = x3
                else:
                    delta /= 2.0
        if np.linalg.norm(x2 - x0) < eps:
            break
    return x2


result = hooke_jeeves(f, [1, 1])
result = hooke_jeeves(ff, np.array([-1, 2, -3]))
print('Минимум:', result)
