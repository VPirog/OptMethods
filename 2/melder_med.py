import numpy as np
from scipy.optimize import minimize


# objective function
def f(x):
    return 3 * x[0] ** 2 + 5 * x[1] ** 2 + 4 * x[2] ** 2 + 2 * x[0] * x[1] - x[0] * x[2] - x[1] * x[2] + 7 * x[0] + x[2]


def nelder_mead(alpha=1, beta=0.5, gamma=2, maxiter=1000):
    # initialization
    v1 = np.array([0, 0, 0])
    v2 = np.array([1.0, 0, 0])
    v3 = np.array([0, 1, 0])
    v4 = np.array([0, 0, 1])

    for i in range(maxiter):
        adict = {tuple(v1): f(v1), tuple(v2): f(v2), tuple(v3): f(v3), tuple(v4): f(v4)}
        points = sorted(adict.items(), key=lambda x: x[1])

        b = np.array(points[0][0])
        g = np.array(points[1][0])
        w = np.array(points[2][0])
        h = np.array(points[3][0])

        mid = (g + b) / 2

        # reflection
        xr = mid + alpha * (mid - w)
        if f(xr) < f(g):
            w = xr
        else:
            if f(xr) < f(w):
                w = xr
            c = (w + mid) / 2
            if f(c) < f(w):
                w = c
        if f(xr) < f(b):

            # expansion
            xe = mid + gamma * (xr - mid)
            if f(xe) < f(xr):
                w = xe
            else:
                w = xr
        if f(xr) > f(g):

            # contraction
            xc = mid + beta * (w - mid)
            if f(xc) < f(w):
                w = xc

        # update points
        v1 = w
        v2 = g
        v3 = b
    return b


print("Result of Nelder-Mead algorithm: ")
xk = nelder_mead()
print("Best point is: %s" % (xk))
