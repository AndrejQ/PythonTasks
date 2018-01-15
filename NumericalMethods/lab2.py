import numpy as np
import matplotlib.pyplot as plt

def w(x, n, a, b):

    X = [(a + b)/2 + 0.5*(b - a)*np.cos(np.pi*(2*(m+1) - 1)/(2*n)) for m in range(n)]
    #X = [(i+1)*5/n for i in range(n)] # zadanie 1
    #X = [-1 +2*i/n for i in range(n)] #zadanie 2

    answer = 1
    for xi in X:
        answer *= x - xi

    return answer

# Task 1

qual = 1000
x = np.linspace(1, 6, qual)
W1 = [w(i, 3, 1, 6) for i in x]
W2 = [w(i, 5, 1, 6) for i in x]
W3 = [w(i, 10, 1, 6) for i in x]
W4 = [w(i, 20, 1, 6) for i in x]
plt.plot(x, W1, x, W2, x, W3, x, W4)
plt.grid(True)
plt.xlabel('w(x)')
plt.show()

#Task 2

''' Интерполяция по Лагранжу '''

function = lambda x: 1/(1+25*x*x)
X = np.linspace(-1, 1, 1000)
Y = 1/(1+25*X*X)

n = 13  # n из условия для Лагранжа

x = np.linspace(-1, 1, n)
y = 1/(1+25*x*x)

def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1;
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


xnew = np.linspace(np.min(x), np.max(x), 100)
ynew = [lagranz(x, y, i) for i in xnew]
plt.plot(X, Y, x, y, 'o', xnew, ynew, '--r', linewidth=2)
plt.ylim([-2,2])
plt.grid(True)
plt.xlabel('Lagranz')
plt.show()

'''Интерполяция вперед по Ньютону'''

x = xnew
y = ynew
def equalDist(a, b, n):
    length = b - a
    step = length / (n + 2)
    x = []
    for i in range(n + 1):
        x.append(a + step * (i + 1))
    return x


def diffMethod(degree, n):
    # points = equalDist(-1, 1, n)
    res = 0
    for i in range(degree):
        if i == 2:
            res = func1(n[i + 1]) - 2 * func1(n[i]) + func1(n[i - 1]) - res
            break
        res = -res + (func1(n[i + 1]) - func1(n[i]))

    return res


def newton(x, n):
    points = equalDist(-1, 1, n)
    res = points[0]
    q = (x - points[0]) / (abs(points[0] - points[1]))
    for i in range(1, n + 1):
        product = 1
        for j in range(1, n + 1):
            product = product * (q - n + 1)
        res = res + product * diffMethod(i, n) / factorial(i)
    return res


def Newton(t, n, x, y):
    res = y[0]

    for i in range(1, n):

        F = 0;
        for j in range(i + 1):

            den = 1;
            for k in range(i + 1):

                if (k != j):
                    den *= (x[j] - x[k]);

            F += y[j] / den;

        for k in range(i):
            F *= (t - x[k]);
        res += F;

    return res;

n = 7 # n из условия по Ньютону



points = equalDist(-1, 1, n)
ypoints = y = [function(i) for i in points]


y = [Newton(i, n, points, ypoints) for i in x]

n = 14 # n из условия по Ньютону



points1 = equalDist(-1, 1, n)
ypoints1 = y1 = [function(i) for i in points1]


y1 = [Newton(i, n, points1, ypoints1) for i in x]
axes = plt.gca()
axes.set_ylim([-2,2])
plt.plot(x, function(x), x, y, '--r', x, y1, '--g', linewidth=2)
plt.xlabel('Newton')
plt.grid(True)
plt.show()