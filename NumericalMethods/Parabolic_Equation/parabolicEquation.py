from _pytest.config import cmdline
from numpy import linspace, sin, pi, meshgrid
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


# a = 10
# T = 15
# l = 20 * pi
# quality_x = 100
# quality_t = 740
# x = linspace(0, l, quality_x)
# t = linspace(0, T, quality_t)
# h = x[1]
# tau = t[1]
# print('stability', a * tau / h ** 2)
# u = [3 * x]
#
# for n in range(quality_t - 1):
#     u += [[0] + [a * tau ** 1 / h ** 2 * (u[-1][m - 1] - 2 * u[-1][m] + u[-1][m + 1]) + tau * sin(x[m]) + u[-1][m]
#                  for m in range(1, quality_x - 1)] + [0]]
#
# fig, ax = plt.subplots()
#
# line, = ax.plot(x, 3 * x)
#
#
# def animate(i):
#     line.set_ydata(u[1 * i])  # update the data
#     return line,
#
#
# ani = animation.FuncAnimation(fig, animate, interval=1)
# plt.show()
# '''3d'''
# fig1 = plt.figure()
# ac = fig1.gca(projection='3d')
#
# X, Y = meshgrid(x, t)
# surf = ac.plot_surface(X, Y, u, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# ac.set_xlabel('X')
# ac.set_ylabel('t')
# ac.set_zlabel('T')
# plt.show()

a = 10
T = 1
l = 2 * pi
quality_x = 100
quality_t = 1000
x = linspace(0, l, quality_x)
t = linspace(0, T, quality_t)
h = x[1]
tau = t[1]
print('pseudo stability', a * tau / h ** 2)
u = [30 * sin(x)]

for time_layer in range(quality_t - 1):
    A = a * tau / h ** 2
    B = A
    C = 1 + 2 * A
    F = u[time_layer] + tau * sin(x)

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

fig, ax = plt.subplots()

line, = ax.plot(x, 30 * sin(x))


def animate(i):
    line.set_ydata(u[1 * i])  # update the data
    return line,


ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
'''3d'''
fig1 = plt.figure()
ac = fig1.gca(projection='3d')

X, Y = meshgrid(x, t)
surf = ac.plot_surface(X, Y, u, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ac.set_xlabel('X')
ac.set_ylabel('t')
ac.set_zlabel('T')

plt.show()
