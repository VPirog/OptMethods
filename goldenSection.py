def goldenSection(eps=0.001, a0=-10, b0=10):
    func = lambda x: (x ) ** 2
    a, b, epsn = [], [], []
    a.append(a0)
    b.append(b0)
    delta = eps / 2

    for i in range(1000):
        x1 = a[i] + ((3 - 5 ** 0.5) / 2) * (b[i] - a[i])
        x2 = a[i] + ((5 ** 0.5 - 1) / 2) * (b[i] - a[i])
        if func(x1) <= func(x2):
            a.append(a[i])
            b.append(x2)
        else:
            a.append(x1)
            b.append(b[i])
        epsn.append(abs(b[i] - a[i]))
        if epsn[i] < eps:
            return ((a[i] + b[i]) / 2)


print(goldenSection())
