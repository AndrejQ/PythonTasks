from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from numpy import sqrt, sin, cos, pi, array, arctan
from layer_area import aria_function
from furier import decompose


def rotate_to_collinear_to_z(dot, direction):
    if direction[1] == 0:
        angle_yx = pi / 2
    else:
        angle_yx = arctan(direction[0] / direction[1])
    # yx: x -> x cos - y sin; y -> x sin + y cos
    dot[0], dot[1] = dot[0] * cos(angle_yx) - dot[1] * sin(angle_yx), dot[0] * sin(angle_yx) + dot[1] * cos(angle_yx)
    if direction[2] == 0:
        angle_zy = pi / 2
    else:
        angle_zy = arctan(sqrt(direction[0] ** 2 + direction[1] ** 2) / direction[2])
    # zy: y -> y cos - z sin; z -> y sin + z cos
    dot[1], dot[2] = dot[1] * cos(angle_zy) - dot[2] * sin(angle_zy), dot[1] * sin(angle_zy) + dot[2] * cos(angle_zy)
    return dot


def is_in_cube(dot):
    return (dot[0])**2 + (dot[1])**2 + abs(dot[2])**2 < (L_cube / 2) ** 2
    return abs(dot[0]) < L_cube / 1 and abs(dot[1]) < L_cube / 1 and abs(dot[2]) < L_cube / 2


def init_crystal_lattice(N, l):
    dots = []

    for x in range(-N, N):
        for y in range(-N, N):
            for z in range(-N, N):
                xi = x * l
                yi = y * l
                zi = z * l

                # cell of photonic crystal
                dots.append([xi, yi, zi])
                dots.append([xi + l / 2, yi + l / 2, zi])
                dots.append([xi + l / 2, yi, zi + l / 2])
                dots.append([xi, yi + l / 2, zi + l / 2])
    return dots


N = 15
l = 1
L_cube = 2 * N * l / 2 / sqrt(2)
R = l / 2 / sqrt(2)
direction = (1, 1, 1)  # (x_direst, y_direst, z_direst)

print(L_cube, 'l cube')
print(R, 'R')
print(sqrt(3) / 3 / l, 2 * sqrt(6) / 3 * R, 'H')

dots = init_crystal_lattice(N, l)
rotated_dots = []
xs = []
ys = []
zs = []
for dot in dots:
    rotated_dot = rotate_to_collinear_to_z(dot, direction)
    rotated_dot = [round(rotated_dot[0], 8), round(rotated_dot[1], 8), round(rotated_dot[2], 8)]
    if is_in_cube(rotated_dot):
        rotated_dots.append(rotated_dot)
        xs.append(rotated_dot[0])
        ys.append(rotated_dot[1])
        zs.append(rotated_dot[2])

# separating in layers {key ('z' coord) : [dots with 'z' coord]}
layer_dots = {}

for d in rotated_dots:
    if layer_dots.get(d[2]) is None:
        layer_dots[d[2]] = [d]
    else:
        layer_dots[d[2]].append(d)

dielectr_x = []
dielectr_y = []

print(sorted(list(layer_dots.keys())))
print(len(list(layer_dots.keys())))

for i in list(layer_dots.items()):
    dielectr_x.append(i[0])
    dielectr_y.append(len(i[1]))

'''Plotting 2D'''
x, K = aria_function(dielectr_x, dielectr_y, L_cube, R)
decompose(x, K)
# plt.figure()
# plt.grid(True)
# plt.plot(dielectr_x, dielectr_y, 'o')
# plt.show()
'''Plotting 3D'''
print(dielectr_x, dielectr_y, "z and num")
fig1 = plt.figure()
ac = fig1.gca(projection='3d')
ac.scatter(xs, ys, zs, c='red')
# ac.scatter([0], [0], [0], c='green', s=100)
ac.set_xlabel('X')
ac.set_ylabel('Y')
ac.set_zlabel('Z')

plt.show()
