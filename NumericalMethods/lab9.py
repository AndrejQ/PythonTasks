from matplotlib.pyplot import plot, show
from numpy import linspace, cos, tan



def shitan():
    N = 100
    x = linspace(0, 1, N)
    h = 1 / N
    eps = 0.001

    def func(x, y):
        return 1 / cos(x) - y * tan(x)


    u = []
    u.append(1)
    for i in range(3):
        k0 = func(x[i], u[i])
        k1 = func(x[i] + h / 2, u[i] + h * k0 / 2)
        k2 = func(x[i] + h / 2, u[i] + h * k1 / 2)
        k3 = func(x[i] + h, u[i] + h * k2)
        nextU = u[i] + h / 6 * (k0 + 2 * k1 + 2 * k2 + k3)
        u.append(nextU)

    for i in range(3, len(x) - 1):
        firstU = u[i] + h / 24 * (
            55 * func(x[i], u[i]) - 59 * func(x[i - 1], u[i - 1]) + 37 * func(x[i - 2], u[i - 2]) - 9 * func(x[i - 3],
                                                                                                             u[i - 3]))
        secondU = u[i] + h / 24 * (
            9 * func(x[i + 1], firstU) + 19 * func(x[i], u[i]) - 5 * func(x[i - 1], u[i - 1]) + func(x[i - 2], u[i - 2]))
        while abs(secondU - firstU) > eps:
            firstU = secondU
            secondU = u[i] + h / 24 * (
                9 * func(x[i + 1], firstU) + 19 * func(x[i], u[i]) - 5 * func(x[i - 1], u[i - 1]) + func(x[i - 2],
                                                                                                         u[i - 2]))
        u.append(secondU)

    return (x, u)

# plot(x, u)
# show()