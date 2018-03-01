import matplotlib.pyplot as plt
from numpy import array, cos, sin, sqrt, log, arctan, pi, linspace, meshgrid
from numpy.random import random, uniform
from mpl_toolkits.mplot3d import Axes3D


# returns array of pair of dots
def emitter(n, xtr, ytr):
    output = []
    counter = 0
    while counter < n:
        x_begin = uniform(xtr[2], xtr[1])
        y_begin = uniform(ytr[1], ytr[0])
        z_begin = 0
        if is_in_triangle(x_begin, y_begin, xtr, ytr):
            counter += 1
            point = end_point(x_begin, y_begin, z_begin)
            x_end = point[0]
            y_end = point[1]
            z_end = point[2]

            X = array([x_begin, x_end])
            Y = array([y_begin, y_end])
            Z = array([z_begin, z_end])

            output.append([X, Y, Z])
    return output


def end_point(x, y, z):
    r = 30
    sigma = 1
    L = - 10 * log(random()) / sigma
    L = 2
    phi = uniform(0, 2 * pi)
    ksi = pi - arctan(y / x)
    l_1 = sqrt(x * x + y * y)
    b = -2 * l_1 * cos(phi + ksi)
    c = l_1 ** 2 - r ** 2
    discriminant = b ** 2 - 4 * c
    # dist between start point and  cylinder
    l_2 = (-b + sqrt(discriminant)) / 2
    alpha = uniform(0, pi / 2)
    x_end = x + L * cos(alpha) * cos(phi)
    y_end = y + L * cos(alpha) * sin(phi)
    # need fixes for l_2
    # x_end = x + l_2 * cos(phi)
    # y_end = y + l_2 * sin(phi)
    z_end = L * sin(alpha)
    if alpha < arctan(20 / l_2):
        if L * cos(alpha) > l_2:
            x_end *= l_2 / (L * cos(alpha))
            y_end *= l_2 / (L * cos(alpha))
            z_end *= l_2 / (L * cos(alpha))
    else:
        if z_end > 20:
            x_end *= 20 / z_end
            y_end *= 20 / z_end
            z_end *= 20 / z_end
    # print(x_end, y_end, x + l_2 * cos(phi), y + l_2 * sin(phi))
    return [x_end, y_end, z_end]


def is_in_triangle(x, y, xtr, ytr):
    if y < ytr[1] or y > ytr[0] or abs(x) > xtr[1]:
        return False
    elif x < xtr[0]:
        if y < sqrt(3) * x + ytr[0]:
            return True
    elif x > xtr[0]:
        if y < - sqrt(3) * x + ytr[0]:
            return True
    else:
        return False


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Triangle
N = 3
r_op = 35 / sqrt(3)
Xtr = array([0, cos(pi / 6) * r_op, -cos(pi / 6) * r_op])
Ytr = array([1 * r_op, -sin(pi / 6) * r_op, -sin(pi / 6) * r_op])
Ztr = array([0, 0, 0])
ax.plot_trisurf(Xtr, Ytr, Ztr, color='red')

# Cylinder
x = linspace(-35, 35, 100)
z = linspace(0, 20, 100)
Xc, Zc = meshgrid(x, z)
Yc = 35 * sqrt(1 - (Xc / 35) ** 2)

# lines
for pair in emitter(10, Xtr, Ytr):
    X = pair[0]
    Y = pair[1]
    Z = pair[2]
    ax.plot(X, Y, Z, color='green')

# Draw parameters
rstride = 20
cstride = 10
ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)
ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
