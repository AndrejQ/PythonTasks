from numpy.random import uniform as uni

qual = 1000000
result = 0
for i in range(qual):
    x = uni(-3, 3)
    y = uni(-3, 3)
    z = uni(-3, 3)

    if x ** 2 + y ** 2 < 9 and z ** 2 + y ** 2 < 9:
        result += 1

print(6 ** 3 * result / qual)
