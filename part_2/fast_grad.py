from part_1 import golden_section
from example import *

alpha_min = 0.1
alpha_max = 1.0


def gradient_descent(x0, eps):
    x = x0
    i = 0
    while True:
        f_alpha = lambda alpha: f(x - alpha * grad_f(x))
        alpha = golden_section(f_alpha, alpha_max, alpha_min)
        x_new = x - alpha * grad_f(x)
        if np.linalg.norm(x_new - x) < eps:
            print(i)
            return x_new
        x = x_new
        i += 1


def gradient(x0, eps):
    x = x0
    alpha_prev = 0
    i = 0
    while True:
        alpha = alpha_min
        while f(x - alpha * grad_f(x)) >= f(x) and alpha >= 1e-8:
            alpha /= 2
        if alpha < 1e-8:
            break
        x_new = x - alpha * grad_f(x)
        if np.linalg.norm(x_new - x) < eps:
            print(i)
            return x_new
        if f(x_new) >= f(x):
            alpha = alpha_prev / 2
            x_new = x - alpha * grad_f(x)
            if np.linalg.norm(x_new - x) < eps:
                print(i)
                return x_new
        alpha_prev = alpha
        x = x_new
        i += 1


x_list = [np.array([1, 2, 3])]
a = 0.001
eps = 10 ** (-4)
print("func_min = ", f(gradient_descent(np.array([1, 1, 1]), eps)), "; x_min = ", gradient_descent(np.array([1, 1, 1]), eps))

print("func_min = ", f(gradient(np.array([1, 1, 1]), eps)), "; x_min = ", gradient(np.array([1, 1, 1]), eps))

