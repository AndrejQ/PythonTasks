import numpy as np

f = lambda x: 1/((x + 1) * (np.sqrt(x*x + 1)))

def rectangle(h):
    x = np.linspace(0, 0.75, round(0.75/h))
    I = 0
    for i in range(len(x) - 1):
        I += f(x[i] + h/2)
    return I*h

def traps(h):
    x = np.linspace(0, 0.75, round(0.75 / h))
    I = 0
    for i in range(len(x) - 1):
        I += f(x[i])*h + h*(f(x[i]+h)-f(x[i]))/2
    return I

def simpson(h):
    x = np.linspace(0, 0.75, round(0.75 / h))
    I = 0
    for i in range(len(x) - 2):
        I += h/3*(f(x[i]) + 4 * f(x[i]+h) + f(x[i] + 2 * h))
    return I/2


def richardson(h):
    s1 = rectangle(h)
    s2 = rectangle(2*h)
    s3 = rectangle(3*h)
    s4 = rectangle(4*h)
    p2 = (s4 - s2)/(s2 - s1)
    return (p2 * s1 - s2)/(p2 - 1)


print('rectanlge')
print(rectangle(0.01))
print(rectangle(0.0001))
print(rectangle(0.000001))
print('trapecio')
print(traps(0.01))
print(traps(0.0001))
print(traps(0.000001))
print('simpson')
print(simpson(0.01))
print(simpson(0.0001))
print(simpson(0.000001))
print('richardson')
print(richardson(0.01))
print(richardson(0.0001))
print(richardson(0.000001))