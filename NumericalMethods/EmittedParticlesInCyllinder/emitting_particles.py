import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

# fig1 = plt.figure()
# fig2 = plt.figure()
# ax = fig1.add_subplot(111, projection='3d')
# ad = fig2.add_subplot(111)

# Parameters of cylinder
r = 30
h = 20
# Parameters of triangle
a = 20
b= 10
r_op = 35 / np.sqrt(3)  # opisannaya okr
xtr = np.array([0, np.cos(np.pi / 6) * r_op, -np.cos(np.pi / 6) * r_op])
ytr = np.array([1 * r_op, -np.sin(np.pi / 6) * r_op, -np.sin(np.pi / 6) * r_op])
# Parameter of mean free path

# without density
# sigma = 0.04172

# with density
sigma = 0.4731

# Quantity of particles
n = 1000
# List of initial points
x0 = []
y0 = []
# List of final points
x1 = []
y1 = []
z1 = []


# Get initial points
def initialPoints():
    global n, x0, y0, b, a
    counter = 0
    while counter < n:
        x = np.random.uniform(xtr[2], xtr[1])
        y = np.random.uniform(ytr[1], ytr[0])
        if is_in_triangle(x, y):
            counter += 1
            x0.append(x)
            y0.append(y)


def is_in_triangle(x, y):
    if y < ytr[1] or y > ytr[0] or abs(x) > xtr[1]:
        return False
    elif x < xtr[0]:
        if y < np.sqrt(3) * x + ytr[0]:
            return True
    elif x > xtr[0]:
        if y < - np.sqrt(3) * x + ytr[0]:
            return True
    else:
        return False


# Get final points
def emitter(setInBound):
    global h, n, r, x1, y1, z1
    for i in range(n):
        phi = 2 * np.pi * np.random.random()
        cosTeta = np.random.random()
        l = -1 / sigma * math.log(np.random.random())
        x = x0[i] + l * np.sqrt(1 - pow(cosTeta, 2)) * np.cos(phi)
        y = y0[i] + l * np.sqrt(1 - pow(cosTeta, 2)) * np.sin(phi)
        z = l * cosTeta
        x1.append(x)
        y1.append(y)
        z1.append(z)


# Draw hedgehog
def drawing():
    global a, b, r, h, n, x0, y0, x1, y1, z1  # , ax, ad
    fig1 = plt.figure()
    fig2 = plt.figure()
    ax = fig1.add_subplot(111, projection='3d')
    ad = fig2.add_subplot(111)
    #Ellipse
    x_ellipse = np.linspace(-a, a, 100)
    y_ellipse = b * np.sqrt(1 - x_ellipse ** 2 / a ** 2)
    ad.plot(xtr, ytr)
    ad.plot([xtr[0], xtr[2]], [ytr[0], ytr[2]], color='blue')
    ad.plot(x0, y0, '.')

    # Cylinder
    x_cylinder = np.linspace(-r, r, 100)
    z_cylinder = np.linspace(0, h, 100)
    Xc, Zc = np.meshgrid(x_cylinder, z_cylinder)
    Yc = r * np.sqrt(1 - (Xc / r) ** 2)

    # Lines
    for i in range(n):
        X = np.array([x0[i], x1[i]])
        Y = np.array([y0[i], y1[i]])
        Z = np.array([0, z1[i]])
        ax.plot(X, Y, Z, linewidth=1, color='green')

    # Draw parameters
    rstride = 20
    cstride = 10
    ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride, color='blue')
    ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride, color='blue')
    ax.plot(xtr, ytr)
    ax.plot([xtr[0], xtr[2]], [ytr[0], ytr[2]], color='blue')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()


# Return boolean - is particle in cylinder
def isInArea(x, y, z):
    global r, h
    if (z > h) or (z < 0) or (pow(x, 2) + pow(y, 2) > pow(r, 2)):
        return False
    else:
        return True


initialPoints()

emitter(True)
drawing()
