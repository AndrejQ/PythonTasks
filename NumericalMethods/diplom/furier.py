from matplotlib import pyplot as plt
from numpy import sin, cos, pi, linspace, array, arctan
import numpy

def integral(x, y):
    result = 0
    h = x[1]
    for u in y:
        result += u * h
    return result


def an(n, x, ytr): return integral(x, cos(2 * n * pi * x / x[-1]) * ytr) * 2 / x[-1]
def bn(n, x, ytr): return integral(x, sin(2 * n * pi * x / x[-1]) * ytr) * 2 / x[-1]


# def an(n,x,y): return A1 / pi / n * (sin(pi * n * a / H)) + B1 / pi / n * (- sin(pi * n * a / H))
# def bn(n,x,y): return A1 / pi / n * (- cos(pi * n * a / H) + 1) + B1 / pi / n * (cos(pi * n * a / H) - 1)

H = 6
a = 4

qual = 1000
A1 = 4
B1 = 1
H /= 2
b = H - a

A = A1 - B1
x = linspace(0, 2 * H, qual)

# ступенчатая функция
ytr = []
for i in x:
    if i < a:
        ytr.append(A1)
    else:
        ytr.append(B1)
# парабула
ytr = [abs(3 * i + 2 - i ** 2) for i in x]
ytr = array(ytr)
plt.figure()

y = array([B1 * 0 + an(0.0001, x, ytr) / 2 for i in range(qual)])
for n in range(1, 50):
    y = y + an(n, x, ytr) * cos(pi * n * x / H)
    y = y + bn(n, x, ytr) * sin(pi * n * x / H)
    if n % 1 == 0:
        plt.plot(x, y)

print(an(1, x, ytr), bn(1, x, ytr))
C = an(1, x, ytr) / cos(arctan(- bn(1, x, ytr) / an(1, x, ytr)))
print(C)

# print(x[-1], H)

plt.plot(x, ytr)
plt.show()
