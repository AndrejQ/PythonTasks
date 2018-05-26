from numpy.random import random, randint
from numpy import linspace, array, log
from matplotlib import pyplot as plt


def two_new_points(xy1, xy2, xy3):
    x1 = xy1[0]
    y1 = xy1[1]
    x2 = xy2[0]
    y2 = xy2[1]
    x3 = xy3[0]
    y3 = xy3[1]
    return [[x1 + 2 / 3 * (x2 - x1), y1 + 2 / 3 * (y2 - y1)], [x2 + 1 / 3 * (x3 - x2), y2 + 1 / 3 * (y3 - y2)]]


iterations_m = []

M = [[50, -50], [-50, -50], [-50, 50], [50, 50], [50, -50], [-50, -50]]
iterations_m.append(M)
for iter in range(15):
    M = []
    for i in range(1, len(iterations_m[iter]) - 1):
        two_points = two_new_points(iterations_m[iter][i - 1], iterations_m[iter][i], iterations_m[iter][i + 1])
        M.append(two_points[0])
        M.append(two_points[1])
    iterations_m.append(M)

plt.figure()
for M in iterations_m:
    plt.plot([M[i][0] for i in range(len(M))], [M[i][1] for i in range(len(M))])
# plt.plot([iterations_m[0][i][0] for i in range(len(iterations_m[0]))], [iterations_m[0][i][1] for i in range(len(iterations_m[0]))], '-o')
plt.plot([iterations_m[-1][i][0] for i in range(len(M))],
         [iterations_m[-1][i][1] for i in range(len(iterations_m[-1]))], '--', color='black', linewidth=3)
plt.show()
'''
# plot
plt.figure()
plt.plot([iterations_m[-1][i][0] for i in range(len(M))],
         [iterations_m[-1][i][1] for i in range(len(iterations_m[-1]))],'.')
plt.plot([iterations_m[-1][i][0] for i in range(len(M))],
         [-iterations_m[-1][i][1] for i in range(len(iterations_m[-1]))],'.', color='blue')
plt.show()
'''
M = iterations_m[-1]
for i in reversed(range(len(M))):
    if M[i][1] < 0:
        M.pop(i)

M = sorted(M, key=lambda x: x[0])
print(M)

M.append([50.1, -10])
integral = 0
for i in range(len(M) - 1):
    integral += (M[i][1] + M[i + 1][1]) / 2 * (M[i + 1][0] - M[i][0])
print(2 * integral, 100 * 100)

plt.figure()
plt.grid(True)
plt.plot([M[i][0] for i in range(len(M) - 2)], [(M[i + 1][1] - M[i][1]) / (M[i + 1][0] - M[i][0]) for i in range(len(M) - 2)])
plt.show()
