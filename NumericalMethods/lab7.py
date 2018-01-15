from random import random as rnd, uniform
from numpy import sqrt
from numpy import cbrt

f1 = lambda x: 1/x
f2 = lambda x: 1/x**2
N = 10000
sum1 = 0
sum2 = 0
for i in range(N):
    rp = cbrt(rnd())
    mu = 2*rnd() - 1
    rq = cbrt(rnd())
    sum1 += f1(sqrt(rp**2 + rq**2 - 2 * mu * rq * rp))
    sum2 += f2(sqrt(rp**2 + rq**2 - 2 * mu * rq * rp))

I1 = 16/9*sum1/N
I2 = 16/9*sum2/N
print(I1, I2)

sum1 = 0
sum2 = 0
for i in range(N):
    rp = cbrt(rnd())
    mu = 2*rnd() - 1
    rq = cbrt(rnd())
    l = rp * mu + sqrt((rp * mu)**2 - (rp**2 - 1))
    ro = uniform(0, l)
    sum1 += ro**2 * f1(ro) * l
    sum2 += ro**2 * f2(ro) * l

I1 = 16/3*sum1/N
I2 = 16/3*sum2/N
print(I1, I2)