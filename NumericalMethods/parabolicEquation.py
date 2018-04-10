from numpy import linspace, sin, arange
from matplotlib import pyplot as plt
import matplotlib.animation as animation

a = 10
T = 15
l = 20
quality_x = 10
quality_t = 100
x = linspace(0, l, quality_x)
t = linspace(0, T, quality_t)
h = x[1]
tau = t[1]
print('stability', a * tau / h ** 2)
u = [3 * x]
# boundary conditions
# u[0][-1] = 0

for n in range(quality_t - 1):
    u += [[0] + [a * tau ** 1 / h ** 2 * (u[-1][m - 1] - 2 * u[-1][m] + u[-1][m + 1]) + tau * sin(x[m]*0) + u[-1][m]
                 for m in range(1, quality_x - 1)] + [0]]

fig, ax = plt.subplots()

line, = ax.plot(x, 3 * x)


def animate(i):
    line.set_ydata(u[1 * i])  # update the data
    return line,


ani = animation.FuncAnimation(fig, animate, interval=100)

plt.show()

a = 10
T = 15
l = 20
quality_x = 10
quality_t = 100
x = linspace(0, l, quality_x)
t = linspace(0, T, quality_t)
h = x[1]
tau = t[1]
print('pseudo stability', a * tau / h ** 2)
u = [3 * x]
# boundary conditions
# u[0][-1] = 0

for time_layer in range(quality_t - 1):
    A = tau / h ** 2
    B = A
    C = 1 + 2 * tau / h ** 2
    F = u[time_layer] + tau * sin(x*0)

    alpha = [0, B / C]
    beta = [0, F[0]]
    for i in range(1, len(x) - 1):
        beta.append((A * beta[-1] + F[i]) / (C - A * alpha[-1]))
        alpha.append(-B / (-C + A * alpha[-1]))

    u.append([0 for i in range(len(x))])
    u[time_layer + 1][-1] = 0
    for i in reversed(range(len(x) - 1)):
        u[time_layer + 1][i] = alpha[i + 1] * u[time_layer + 1][i + 1] + beta[i + 1]
    u[time_layer + 1][0] = 0


# plt.figure()
# for i in range(10):
#     plt.plot(x, u[10 * i])
# plt.show()
fig, ax = plt.subplots()

line, = ax.plot(x, 3 * x)


def animate(i):
    line.set_ydata(u[1 * i])  # update the data
    return line,


ani = animation.FuncAnimation(fig, animate, interval=100)

plt.show()