from example import *


def nelder_mead(f, x0, alpha=1, beta=0.5, gamma=2, maxiter=10000, tol=1e-6):
    # инициализация
    n = len(x0)
    v = np.zeros((n + 1, n))
    f_values = np.zeros(n + 1)

    # инициализируем вершины
    v[0] = x0
    for i in range(n):
        x = x0.copy()
        x[i] += 1
        v[i + 1] = x

    for i in range(maxiter):
        # вычисляем значения функции на каждой вершине
        for j in range(n + 1):
            f_values[j] = f(v[j])

        # сортируем вершины по значению функции
        order = np.argsort(f_values)
        v = v[order]

        # проверяем, достигнута ли сходимость
        if np.abs(f_values[order[0]] - f_values[order[-1]]) < tol:
            return v[0]

        # вычисляем центр масс всех вершин, кроме самой худшей
        xc = np.mean(v[:-1], axis=0)

        # отражение
        xr = xc + alpha * (xc - v[-1])
        fxr = f(xr)
        if f_values[order[0]] <= fxr < f_values[order[-2]]:
            v[-1] = xr
            continue

        # расширение
        if fxr < f_values[order[0]]:
            xe = xc + gamma * (xr - xc)
            fxe = f(xe)
            if fxe < fxr:
                v[-1] = xe
            else:
                v[-1] = xr
            continue

        # сжатие
        xc = np.mean(v[:-1], axis=0)
        if fxr >= f_values[order[-2]]:
            if fxr < f_values[-1]:
                xc = np.mean(v[:-1], axis=0)
                xc = xc + beta * (xr - xc)
                fxc = f(xc)
                if fxc <= fxr:
                    v[-1] = xc
                    continue

        # уменьшаем вектор
        for i in range(1, n + 1):
            v[i] = v[0] + 0.5 * (v[i] - v[0])

    return v[0]


# print(nelder_mead(f, np.array([0, 0, 0])))
#
# print(nelder_mead(f, np.array([0, 0])))
