import matplotlib.pyplot as plt
from numpy import array, cos, sin, tan, sqrt, log, arctan, pi, linspace, meshgrid
from numpy.random import random, uniform
from mpl_toolkits.mplot3d import Axes3D

particles = 100


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
    r = 35
    sigma = 0.1
    L = - log(random()) / sigma
    L = 50
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
    z_end = L * sin(alpha)

    x_y_end = binary_shortener(x, y, phi, r)
    l_2 = sqrt((x - x_y_end[0]) ** 2 + (y - x_y_end[1]) ** 2)
    if x_end ** 2 + y_end ** 2 > r ** 2 or z_end > 20:
        if tan(alpha) < (20 / l_2):
            z_end *= abs(l_2 / (L * cos(alpha)))
            x_end = x_y_end[0]
            y_end = x_y_end[1]
            # if L * cos(alpha) > l_2:
            #     x_end *= l_2 / (L * cos(alpha))
            #     y_end *= l_2 / (L * cos(alpha))
            #     z_end *= l_2 / (L * cos(alpha))
        else:
            if z_end > 20:
                x_end *= 20 / z_end
                y_end *= 20 / z_end
                z_end *= 20 / z_end
            if x_end ** 2 + y_end ** 2 > r ** 2:
                podobie = l_2 / ((x - x_end) ** 2 + (y - y_end) ** 2)
                z_end *= podobie
                x_end *= podobie
                y_end *= podobie

    return [x_end, y_end, z_end]


def binary_shortener(x, y, phi, r):
    d = 71
    d_previous = 0
    eps = 0.00001
    x_new = x + d * cos(phi)
    y_new = y + d * sin(phi)
    while abs(x_new ** 2 + y_new ** 2 - r ** 2) > eps:
        if x_new ** 2 + y_new ** 2 > r ** 2:
            d = d - (d - d_previous) / 2
            x_new = x - d * cos(phi)
            y_new = y - d * sin(phi)
        else:
            d, d_previous = d + (d - d_previous) / 2, d
            x_new = x - d * cos(phi)
            y_new = y - d * sin(phi)
    return [x_new, y_new]


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
emitted_particles = emitter(particles, Xtr, Ytr)
for pair in emitted_particles:
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


# # draw 2d triangle
fig_2d = plt.figure()
plt.plot(Xtr, Ytr)
plt.plot([Xtr[0], Xtr[2]], [Ytr[0], Ytr[2]], color='blue')
x_start_coords = [i[0][0] for i in emitted_particles]
y_start_coords = [i[1][0] for i in emitted_particles]
plt.plot(x_start_coords, y_start_coords, 'o')


plt.show()
