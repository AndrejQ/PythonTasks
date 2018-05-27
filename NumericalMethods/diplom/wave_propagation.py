from copy import deepcopy
from numpy.random import randint
from numpy import cos, linspace, sqrt, zeros
from matplotlib import pyplot as plt


# wave = [Amplitude, k, phase]
def wave_propagate(position, wave, depth):
    if position < 0:
        return
    elif position >= len(eps_x) - 1 or depth == 0:
        waves[position].append(wave)
        return
    else:
        if wave[1] < 0:
            waves[position].append(wave)
            n1 = n[position][0]
            n2 = n[position + 1][0]
            # propagate ->
            wave_propagate(position + 1, [wave[0] * 2 * n1 / (n1 + n2),
                                          wave[1] / n1 * n2,
                                          wave[2] + points[position + 1] * (wave[1] - wave[1] / n1 * n2)],
                           depth - 1)
            # wave_propagate(position + 1, [wave[0],
            #                               wave[1] / n1 * n2,
            #                               wave[2] + points[position + 1] * (wave[1] - wave[1] / n1 * n2)],
            #                depth - 1)

            # reflecting
            wave_propagate(position, [wave[0] * (n1 - n2) / (n1 + n2),
                                      -wave[1],
                                      wave[2] + 2 * wave[1] * points[position + 1]],
                           depth - 1)
            # wave_propagate(position, [wave[0] / 1.05,
            #                           -wave[1],
            #                           wave[2] + 2 * wave[1] * points[position + 1]],
            #                depth - 1)

        else:
            # propagation <-
            waves[position].append(wave)
            n1 = n[position][0]
            n2 = n[position - 1][0]
            # propagate <-
            wave_propagate(position - 1, [wave[0] * 2 * n1 / (n1 + n2),
                                          wave[1] / n1 * n2,
                                          wave[2] + points[position] * (wave[1] - wave[1] / n1 * n2)],
                           depth - 1)
            # wave_propagate(position - 1, [wave[0]/1.0,
            #                               wave[1] / n1 * n2,
            #                               wave[2] + points[position] * (wave[1] - wave[1] / n1 * n2)],
            #                depth - 1)

            # reflecting
            wave_propagate(position, [wave[0] * (n1 - n2) / (n1 + n2),
                                      -wave[1],
                                      wave[2] + 2 * wave[1] * points[position]],
                           depth - 1)
            # wave_propagate(position, [wave[0] / 1.05,
            #                           -wave[1],
            #                           wave[2] + 2 * wave[1] * points[position]],
            #                depth - 1)


c = 1
w = 1.2
a = 2
t = 13
n1 = 1
n2 = 3
Em = 1
qual = 200
x = linspace(-2, 2, qual)
#  ->
E1 = Em * cos(w * t - w * x)
E2 = (n1 - n2) / (n1 + n2) * Em * cos(w * t + w * (x - 2 * a))
x3 = linspace(2, 4, qual)
E3 = 2 * n1 / (n1 + n2) * Em * cos(w * t - w * x3)

# [[eps1, l1], [eps2, l2], [eps3, l3]]
eps_x = [[n1 ** 2, 2], [n2 ** 2, 2], [n1 ** 2, 2], [n2 ** 2, 2], [n1 ** 2, 2], [n2 ** 2, 2], [n1 ** 2, 2], [n2 ** 2, 2]]
# [[n1, l1], [n2, l2], [n3, l3]]
n = deepcopy(eps_x)
# eps(x) -> n(x)
for i in range(len(eps_x)):
    n[i][0] = sqrt(n[i][0])

depth_of_crystal = sum([i[1] for i in eps_x])
print('eps', eps_x)
print('n', n)
# districts of waves
waves = [[] for i in eps_x]

# from [l1, l2, l3...] to [0, l1, l1 + l2, l1 + l2 + l3, ...]
points = [0]
for i in range(len(eps_x)):
    points.append(points[-1] + eps_x[i][1])

wave_propagate(0, [Em, -w / c * n[0][0], w * t], 19)

print('points', points)
# print('wawes', waves)
plt.figure()
plt.grid(True)
counter = 0
for area in waves:
    qual_in_area = int(qual * eps_x[counter][1] / depth_of_crystal)
    y = zeros(qual_in_area)
    x = linspace(points[counter], points[counter + 1], qual_in_area)
    for wave in area:
        Emax = wave[0]
        k = wave[1]
        phase = wave[2]
        y = y + Emax * cos(k * x + phase)
        # y = Em * cos(k * x + phase)
        # plt.plot(x, y)
    plt.plot(x, y, color='black', linewidth=2)
    counter += 1

# drawing vertical lines for each eps(x)
for i in points:
    plt.plot([i, i], [-Em*1.5, Em*1.5], color='black', linewidth=1)

plt.xlabel('x, mkm')
plt.ylabel('E, V/m')
plt.show()
