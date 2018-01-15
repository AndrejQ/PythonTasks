from numpy import pi, linspace, sin, cos
from matplotlib import pyplot as plt

a = 0
b = pi / 2
qual = 100
x = linspace(a, b, qual)
h = (b - a) / qual

ai = 1
bi = -2 + h ** 2
gi = 1
di = h ** 2

y = [0]
A = [0]
B = [0]

for i in range(qual - 1):
    B.append((di - gi * B[-1]) / (bi + gi * A[-1]))
    A.append(-ai/(bi + gi * A[-1]))
    y += [0]

for i in range(qual):
    y[-i-1] = A[-i-1] * y[-i] + B[-i-1]

plt.plot(x, y, 'o', label = 'progon')
plt.plot(x, -sin(x) - cos(x)+1, label = 'analyt')
plt.legend(loc = 'upper left')
plt.show()

