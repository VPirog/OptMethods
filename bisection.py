def bisection(eps=0.001, a0=-10, b0=10):
    func = lambda x: (x - 2) ** 2
    a, b, epsn = [], [], []
    a.append(a0)
    b.append(b0)
    delta = eps / 2

    for i in range(1000):
        x1 = (a[i] + b[i] - delta) / 2
        x2 = (a[i] + b[i] + delta) / 2
        if func(x1) <= func(x2):
            a.append(a[i])
            b.append(x2)
        else:
            a.append(x1)
            b.append(b[i])
        epsn.append((b[0] - a[0] - delta) / 2 ** (i + 1) + delta / 2)
        if epsn[i] < eps:
            print((a[i] + b[i]) / 2)
            break


bisection()
