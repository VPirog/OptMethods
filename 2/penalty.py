import numpy as np
from scipy.optimize import minimize


# objective function
def f(x):
    return 10 * x[0] ** 2 + 3 * x[0] * x[1] + x[1] ** 2 + 10 * x[1]


# penalty function
def P(x, t):
    return t * (x[0] + x[1] - 2) ** 2


# combined objective and penalty function
def F(x, t):
    return f(x) + P(x, t)


# initial guess
x0 = np.array([0, 0])

# penalty coefficient
t = 1

# optimization loop
for i in range(10):
    # minimize combined function using Nelder-Mead
    res = minimize(lambda x: F(x, t), x0, method='Nelder-Mead')
    x0 = res.x
    t *= 10

# print results
print("Result of Penalty method: ")
print("Best point is: %s" % (x0))
print("Minimum value is: %s" % (f(x0)))
