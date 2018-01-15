from matplotlib import pyplot as plt
from numpy import sin, exp, sqrt, linspace, pi, log
from random import random as rnd
from random import uniform as uni


N = 0
n = 0

qual = 10000

x2 = linspace(0, pi / 2, qual)
y2 = sin(x2)

xr = [rnd() for i in range(qual)]
yr = [rnd() for i in range(qual)]

# counting 1st integral ================================ 111111111111
norma = 1/3
for i in range(qual):
    if yr[i] < norma * exp(xr[i]):
        N += 1
        n += 1
    else:
        N += 1

print('inegral 1 geometric = ', 1 / norma * n / N)



summ = 0
for i in range(qual):
    summ += exp(xr[i])
print('inegral 1 uniform = ', summ / qual)



summ = 0
for i in range(qual):
    summ += exp(sqrt(xr[i])) / (2 * sqrt(xr[i]))
print('inegral 1 linear = ', summ / qual)


summ = 0
for i in range(qual):
    summ += (exp(xr[i]) + exp(1 - xr[i]))/2
print('inegral 1 sim = ', summ / qual)


print('=====================================================================')
# counting 2nd integral =========================================== 2222222


N = 0
n = 0

xr = [uni(0, pi / 2) for i in range(qual)]
yr = [uni(0, pi / 2) for i in range(qual)]
norma = pi / 2
for i in range(qual):
    if yr[i] < sin(xr[i]):
        N += 1
        n += 1
    else:
        N += 1

print('inegral 2 geometric = ', norma * norma * n / N)

summ = 0
c = 2 / pi
for i in range(qual):
    summ += sin(xr[i]) / c
print('inegral 2 uniform = ', summ / qual)


summ = 0
c = 8 / pi**2
for i in range(qual):
    summ += sin(sqrt(xr[i])) / (c * sqrt(xr[i]))
print('inegral 2 linear = ', summ / qual)


N = 0
n = 0

xr = [uni(0, pi / 2) for i in range(qual)]
yr = [uni(0, pi / 2) for i in range(qual)]
norma = pi / 2
for i in range(qual):
    if yr[i] < (sin(xr[i]) + sin(pi/2 - xr[i]))/2:
        N += 1
        n += 1
    else:
        N += 1

print('inegral 2 sim = ', norma * norma * n / N)


print('=====================================================================')
# countin previous integral========================================== previous 3333333

N = 0
n = 0

xr = [rnd() for i in range(qual)]
yr = [rnd() for i in range(qual)]

f = lambda x: 1/((x + 1) * (sqrt(x*x + 1)))
norma = 0.75
for i in range(qual):
    if yr[i] < f(xr[i] * norma):
        N += 1
        n += 1
    else:
        N += 1


print('inegral 3 geometric = ', norma * n / N)
xr = [rnd() for i in range(qual)]
yr = [rnd() for i in range(qual)]
for i in range(qual):
    if yr[i] < f(xr[i] * norma):
        N += 1
        n += 1
    else:
        N += 1

print('inegral 3 sim = ', norma * n / N)


xr = [uni(0, 0.75) for i in range(qual)]
yr = [uni(0, 0.75) for i in range(qual)]

summ = 0
c = 1/0.75
ksi = lambda x: - log(1 - x/c)
for i in range(qual):
    summ += f(xr[i]) / c
print('inegral 3 uniform = ', summ / qual)


summ = 0
c = 1 / (1-exp(- 0.75))
ksi = lambda x: - log(1 - x/c)
for i in range(qual):
    summ += f(ksi(xr[i])) / (c * exp(-ksi(xr[i])))
print('inegral 3 exponencial = ', summ / qual)



print('=====================================================================')


xr = [rnd() for i in range(1000)]
yr = [rnd() for i in range(1000)]

xr1 = []
for i in xr:
    xr1.append(sqrt(i*(pi**2)/4))
yr1 = []
for i in yr:
    yr1.append(sqrt(i*(pi**2)/4))
plt.figure()
plt.plot(xr, yr, 'o')

plt.figure()
plt.plot(xr1, yr, 'o')
#
# x2 = np.linspace(0, np.pi / 2, 1000)
# y2 = np.sin(x2)
# y22 = np.sin(np.pi / 2 - x2)
#
# plt.figure()
# plt.plot(x2, y2, x2, y22, x2, (y2 + y22)/2)
#
plt.show()

