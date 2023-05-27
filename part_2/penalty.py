import numpy as np
from sympy import primerange
from melder_mid import nelder_mead


# def func(x):
#     return x[0] ** 2 + x[1] ** 2
#
#
# def penalty(x, Ak):
#     return Ak * (max(0, x[0] + 9)) ** 2


# Ваша функция f
def func(x):
    return -x[0] + x[1] ** 2 - 2 * x[1]


def penalty(x, Ak):
    return Ak * (max(0, 3 * x[0] ** 2 + 2 * x[1] ** 2 - 6)) ** 2


def objective_with_penalty(x, t):
    return func(x) + penalty(x, t)


# Начальное значение переменных
x0 = np.array([0, 0])


def penalty_method(eps=10 ** (-5), up_list=None):
    if up_list is None:
        up_list = list(range(1, 10000))
    result = []
    print(f"точность равна: {eps}")

    for i, list_i in enumerate(up_list):
        penalty_coefficient = list_i
        # Минимизация функции с штрафными функциями, используя nelder_mead
        result.append(nelder_mead(lambda x: objective_with_penalty(x, penalty_coefficient), x0))
        if i % 2 == 0 and i != 0:
            if np.linalg.norm(result[i] - result[int(i / 2)]) < eps:
                print(f"Число итераций: {i}")
                return result


# Вывод результатов
# formatted_result = np.vectorize(lambda x: "{:.{}f}".format(float(x), j + 1))(result[-1])
# formatted_func_result = np.vectorize(lambda x: "{:.{}f}".format(float(x), j + 1))(func(result[-1]))
# print(formatted_result, formatted_func_result)

print("Optimal solution for exp(i):")
result = penalty_method(up_list=[np.exp(i) for i in range(1, 100)])
print(result[-1], func(result[-1]))
print('\n')

print("Optimal solution for pi * i:")
result = penalty_method(up_list=[np.pi * i for i in range(1, 100000)])
print(result[-1], func(result[-1]))
print('\n')

print("Optimal solution for i ** golden_section_num:")
golden = (1 + 5 ** 0.5) / 2
result = penalty_method(up_list=[golden ** i for i in range(1, 1000)])
print(result[-1], func(result[-1]))
print('\n')

print("Optimal solution for prime numbers:")
result = penalty_method(up_list=primerange(10000))
print(result[-1], func(result[-1]))
print('\n')

print("Optimal solution for exp(primerange(10000))")
result = penalty_method(up_list=[np.exp(i) for i in primerange(100)])
print(result[-1], func(result[-1]))
print('\n')

print("Optimal solution for primenumber ** primenumber")
result = penalty_method(up_list=[i ** i for i in primerange(100)])
print(result[-1], func(result[-1]))
print('\n')

print("Optimal solution for primenumber ** (primenumber * 2)")
result = penalty_method(up_list=[i ** (i * 2) for i in primerange(100)])
print(result[-1], func(result[-1]))
print('\n')

print("Optimal solution for primenumber ** (primenumber * 4)")
result = penalty_method(up_list=[i ** (i * 4) for i in primerange(100)])
print(result[-1], func(result[-1]))
print('\n')

print("Optimal solution:")
result = penalty_method()
print(result[-1], func(result[-1]))
print('\n')
