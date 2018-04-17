from _pytest.config import cmdline
from numpy import linspace, sin, pi, meshgrid, array
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

a = 1.5
T = 200
l = 2 * pi
quality_x = 15
quality_t = 1040
x = linspace(0, l, quality_x)
t = linspace(0, T, quality_t)
h = x[1]
tau = t[1]
print('stability', a * tau / h ** 2)
u = [2 * (array([l]) - x)]

for n in range(quality_t - 1):
    u += [[u[n - 1][0]] + [a * tau / h ** 2 * (u[-1][m - 1] - 2 * u[-1][m] + u[-1][m + 1]) + tau * 2 * sin(x[m]) + u[-1][m]
                 for m in range(1, quality_x - 1)] + [u[n - 1][-1]]]
    u[n][0] = u[n][1]
    u[n][-1] = 0

fig, ax = plt.subplots()

line, = ax.plot(x, 2 * (array([l]) - x))


def animate(i):
    line.set_ydata(u[10 * i])  # update the data
    return line,


ani = animation.FuncAnimation(fig, animate, interval=1)
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