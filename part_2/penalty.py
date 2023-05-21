import numpy as np
from scipy.optimize import minimize
from melder_mid import nelder_mead


# Ваша функция f
def func(x):
    return -x[0] + x[1] ** 2 - 2 * x[1]


def penalty(x, Ak):
    return Ak * (max(0, 3 * x[0] ** 2 + 2 * x[1] ** 2 - 6)) ** 2


def objective_with_penalty(x, t):
    return func(x) + penalty(x, t)


# Начальное значение переменных
x0 = np.array([0, 0])

# Коэффициент штрафа
max_iter = 1000000
result = []
for j in range(1, 7):
    result = []
    eps = 10 ** (-j)
    print(f"точность равна: {eps}")
    for i in range(max_iter):
        penalty_coefficient = i + 1
        # Минимизация функции с штрафными функциями, используя nelder_mead
        result.append(nelder_mead(lambda x: objective_with_penalty(x, penalty_coefficient), x0))
        if i % 2 == 0 and i != 0:
            if np.linalg.norm(result[i] - result[int(i / 2)]) < eps:
                print(f"Число итераций: {i}")
                break

    print("Optimal solution:")
    formatted_result = np.vectorize(lambda x: "{:.{}f}".format(float(x), j + 1))(result[-1])
    formatted_func_result = np.vectorize(lambda x: "{:.{}f}".format(float(x), j + 1))(func(result[-1]))
    print(formatted_result, formatted_func_result)
    print('------------------------')
# Вывод результатов
