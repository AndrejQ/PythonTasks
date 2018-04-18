from matplotlib import pyplot as plt
from numpy import sqrt, linspace, zeros, array, pi

quality = 1000


def globule_area_function(A, B, coord):
    f = pi * (A * coord - B - coord ** 2)
    if f > 0:
        return f
    else:
        return 0


def globule_area(z0, R, x):
    A = 2 * (R + z0)
    B = z0 ** 2 + 2 * z0 * R
    y = array([globule_area_function(A, B, coord) for coord in x])
    return y

def aria_function(z_layer_coord, z_globules_number, L_cube, R):
    x = linspace(-L_cube / 2, L_cube / 2, quality)
    y = zeros(quality)
    for i in range(len(z_layer_coord)):
        y += globule_area(z_layer_coord[i] - R, R, x) * z_globules_number[i] / (L_cube) ** 2 / 4
    plt.figure()
    plt.plot(x, y)
    plt.show()
