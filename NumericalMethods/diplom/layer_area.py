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
    # x = linspace(6 * R, 6 * R, quality)
    y = zeros(quality)
    for i in range(len(z_layer_coord)):
        y += globule_area(z_layer_coord[i] - R, R, x) * z_globules_number[i] / (L_cube) ** 2 / 4
    plt.figure()
    # restricting period
    x=x[10:65]
    y=y[10:65]

    # x = x[33:87]
    # y = y[33:87]
    plt.plot(x, y)
    plt.show()
    # K(x)
    return x, y * (2.1609 - 1) * 0.74048 + 1  # поправка 0.74048
