import numpy as np
from matplotlib.pyplot import plot, show, title, legend
from lab9 import shitan

f = lambda x, u: 1 / np.cos(x) - u * np.tan(x)

k0 = lambda x, u: f(x, u)
k1 = lambda x, u: f(x + h / 2, u + h / 2 * k0(x, u))
k2 = lambda x, u: f(x + h / 2, u + h / 2 * k1(x, u))
k3 = lambda x, u: f(x + h, u + h * k2(x, u))

qual = 100
x = np.linspace(0, 1, qual)
h = 1 / qual
u1 = [1]
u2 = [1]
u3 = [1]
u4 = [1]

for i in x[1:]:
    u1.append(u1[-1] + h * f(i, u1[-1]))
    u2.append(u2[-1] + h / 2 * (f(i, u1[-1]) + f(i + h, u2[-1] + h * f(i, u2[-1]))))
    u3.append(u3[-1] + h * f(i + h / 2, u3[-1] + h / 2 * f(i, u3[-1])))
    u4.append(u4[-1] + h / 6 * (k0(i, u4[-1]) + 2 * k1(i, u4[-1]) + 2 * k0(i, u2[-1]) + k3(i, u4[-1])))

plot(x, u1, label = 'Euler method')
plot(x, u2, label = 'Euler method modified')
plot(x, u3, label = 'Euler method improved')
plot(x, u4, label = 'Runge-Kut')
plot(x, np.sin(x) + np.cos(x), 'k--', label = 'original')
plot(shitan()[0], shitan()[1], '-.', label = 'many steps')
legend(loc = 'upper left')
show()

# plot(x, u1, x, u2, x, u3, x, u4)
# show()

qual = 100
A = 5
h = A / qual
t = np.linspace(0, A, qual)
y = [1]
x = [0]
x1 = [1]
y1 = [0]
x2 = [1]
y2 = [0]
for i in t[1:]:
    # euler
    y.append(y[-1] + h * (-0.2 * y[-1] - x[-1]))
    x.append(x[-1] + h * y[-2])
    # euler-krombacher
    x1.append(x[-1] + h * (-0.2 * x[-1] - y[-1]))
    y1.append(y[-1] + h * x[-1])

w = 10 / 3 / np.sqrt(11)
plot(t, x, t, x1, t, w * np.exp(-0.1 * t) * np.sin(w * t))
show()