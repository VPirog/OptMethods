from example import *

def nelder_mead(f, x0, alpha=1, beta=0.5, gamma=2, maxiter=10000, tol=1e-6):
    # initialization
    n = len(x0)
    v = np.zeros((n + 1, n))
    f_values = np.zeros(n + 1)

    # initialize vertices
    v[0] = x0
    for i in range(n):
        x = x0.copy()
        x[i] += 1
        v[i + 1] = x

    for i in range(maxiter):
        # evaluate function values at each vertex
        for j in range(n + 1):
            f_values[j] = f(v[j])

        # sort vertices by function value
        order = np.argsort(f_values)
        v = v[order]

        # check if converged
        if np.abs(f_values[order[0]] - f_values[order[-1]]) < tol:
            return v[0]

        # calculate center of mass of all vertices except the worst
        xc = np.mean(v[:-1], axis=0)

        # reflection
        xr = xc + alpha * (xc - v[-1])
        fxr = f(xr)
        if f_values[order[0]] <= fxr < f_values[order[-2]]:
            v[-1] = xr
            continue

        # expansion
        if fxr < f_values[order[0]]:
            xe = xc + gamma * (xr - xc)
            fxe = f(xe)
            if fxe < fxr:
                v[-1] = xe
            else:
                v[-1] = xr
            continue

        # contraction
        xc = np.mean(v[:-1], axis=0)
        if fxr >= f_values[order[-2]]:
            if fxr < f_values[-1]:
                xc = np.mean(v[:-1], axis=0)
                xc = xc + beta * (xr - xc)
                fxc = f(xc)
                if fxc <= fxr:
                    v[-1] = xc
                    continue

        # shrink
        for i in range(1, n + 1):
            v[i] = v[0] + 0.5 * (v[i] - v[0])

    # return the best point
    return v[0]


print(nelder_mead(f, np.array([0, 0, 0])))





print(nelder_mead(ff, np.array([0, 0])))
