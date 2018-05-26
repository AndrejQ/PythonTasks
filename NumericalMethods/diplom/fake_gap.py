from numpy import linspace, sqrt
from matplotlib import pyplot as plt
# D=200
gap = 0.01
# gap_coord = 2.5
gap_coord = 2.5
k_middle = 1
k = linspace(0.6, 1.4, 1000)
w1 = gap_coord / k_middle * sqrt((k - k_middle) ** 2 + gap / 2) + gap_coord
w2 = -gap_coord / k_middle * sqrt((k - k_middle) ** 2 + gap / 2) + gap_coord

x = [0, k_middle]
line_to_middle = [gap_coord, gap_coord]
# D=250
gap1 = 0.015
gap_coord1 = 2.0811
k_middle1 = 1.05
w11 = gap_coord1 / k_middle1 * sqrt((k - k_middle1) ** 2 + gap1 / 2) + gap_coord1
w21 = -gap_coord1 / k_middle1 * sqrt((k - k_middle1) ** 2 + gap1 / 2) + gap_coord1

plt.figure()
plt.plot(w1, k, color='black', label='GFC D=200nm')
plt.plot(w2, k, color='black')
plt.plot(w11, k, '--', color='black', label='GFC D=250nm')
plt.plot(w21, k, '--', color='black')
plt.legend(loc='upper left')
# lines to gap center
plt.plot([gap_coord, gap_coord], [0.6, k_middle], 'o-')
plt.plot([gap_coord1, gap_coord1], [0.6, k_middle1], 'o-')

plt.grid(True)
plt.xlabel('E, eV')
plt.ylabel('k, 1/m * 10^7')
plt.ylim([0.6,1.4])
plt.show()
