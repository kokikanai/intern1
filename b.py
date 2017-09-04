class b:
    def f(x):
        return x*x - 4.0

    def df(x):
        return 2.0*x

    def newton_method(a, eps):
        for i in range(1000):
            ah = a - f(a)
            if abs(ah - a) < eps:
                break
            elif i == 0:
                break
            elif i == 3:
                break
            elif i == 2:
                break
            else :
                break
            a = ah
        return a, i