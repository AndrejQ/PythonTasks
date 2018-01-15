import sys
from math import factorial, sqrt

class Polynomial:

    koefficients = []

    def delZeros(self):
        if (self.koefficients == []):
            return Polynomial([0])
        for i in range(len(self.koefficients)):
            if self.koefficients[-1] == 0:
                if (self.koefficients == [0]):
                    return self
                del self.koefficients[-1]
            else:
                return self

    def degree(self):
        return len(self.koefficients) - 1

    def __init__(self, koefficient):
        if (type(koefficient) == list):
            self.koefficients = koefficient
        elif (type(koefficient) == dict):
            self.koefficients = [0] * (max(list(koefficient.keys())) + 1)
            for i in list(koefficient.keys()):
                self.koefficients[i] = koefficient[i]
        elif (type(koefficient) == int or type(koefficient) == float):
            self.koefficients = [koefficient]
        elif (type(koefficient) == Polynomial):
            self.koefficients = koefficient.koefficients

    def __str__(self):
        text = ""
        for i in range(len(self.koefficients)):
            def sign(koef):
                if (koef >= 0):
                    return "+" + str(koef)
                else:
                    return str(koef)

            text += sign(self.koefficients[i]) +'*x^' + str(i)
        return text[0:].replace("*x^0","").replace("+", " + ").replace("-", " - ")

    def __add__(self, other):
        if (type(other) == int or type(other) == float):
            self.koefficients[0] += other
            return self
        if (len(other.koefficients) < len(self.koefficients)):
            for i in range(len(other.koefficients)):
                self.koefficients[i] += other.koefficients[i]
            return self
        else:
            for i in range(len(self.koefficients)):
                other.koefficients[i] += self.koefficients[i]
            return other

    def __sub__(self, other):
        if (len(other.koefficients) < len(self.koefficients)):
            for i in range(len(other.koefficients)):
                self.koefficients[i] -= other.koefficients[i]
            return self
        else:
            kostil = self.koefficients + [0 for i in range(len(other.koefficients) - len(self.koefficients))]
            for i in range(len(other.koefficients)):
                kostil[i] -= other.koefficients[i]
            return Polynomial(kostil)

    def __mul__(self, other):
        if (type(other) == int or type(other) == float):
            return Polynomial([i * other for i in self.koefficients])
        mass = []
        kostil = Polynomial([])
        for i in range(len(self.koefficients)):
            mass.append([0]*i + [self.koefficients[i]*j for j in other.koefficients])
        kostil = Polynomial([])
        for i in mass:
            kostil = kostil + Polynomial(i)
        return kostil

    def __eq__(self, other):
        # print(self)
        # print(other)
        # print('')
        self.delZeros()
        other.delZeros()
        if self.koefficients == other.koefficients:
            return True
        else:
            return False

    def __neg__(self):
        return Polynomial([-i for i in self.koefficients])

    def __mod__(self, other):
        self = self.delZeros()
        other = other.delZeros()
        if (len(self.koefficients) <= 1 or len(self.koefficients) < len(other.koefficients) or self.koefficients == other.koefficients):
            return self
        if (len(other.koefficients) <= 1):
            return Polynomial([0])
        else:
            x_v_stepeni = [self.koefficients[self.degree()] / other.koefficients[other.degree()] if (i == self.degree() - other.degree()) else 0 for i in range(self.degree() - other.degree() + 1)]
            #return x_v_stepeni
            return (self - other * Polynomial(x_v_stepeni)) % other

    def __iter__(self):
        return iter([(i, self.koefficients[i]) for i in range(self.degree() + 1)])

    def __pow__(self, power, modulo=None):
        if (power == 0):
            return Polynomial([1])
        else:
            this = Polynomial(self)
            for i in range(power - 1):
                self = self * this
            return self

    def gcd(self, other):
        if ((self % other).koefficients == [0]):
            return other
        else:
            return other.gcd(self % other)

    def subst(self, x):
        value = 0
        for i in range(self.degree() + 1):
            value += self.koefficients[i]*x**i
        return value

    def der(self, d = 1):
        for j in range(d):
            self.koefficients = [self.koefficients[i + 1] * (i + 1) for i in range(self.degree())]
        return self.delZeros()

    def dersubst(self, x, d = 1):
        return self.der(d).subst(x)

    # def taylor(self, x, d):
    #     taylor_pol = Polynomial([])
    #     for i in range(min(d + 1, self.degree() + 1)):
    #         taylor_pol = taylor_pol + Polynomial({i : self.dersubst(-x, i)/factorial(i)})
    #     return taylor_pol

class RealPolynomial(Polynomial):

    def find_root(self):
        if (self.degree() % 2 == 0):
            print('Exception : Use odd polynom degree for finding root')
            sys.exit()
        else:
            quality = 0.00001
            h = 2**50
            xCurrent = -10*h
            while (h > quality):
                while (self.subst(xCurrent) * self.subst(xCurrent + h) <= 0):
                    h /= 2
                xCurrent += h
            return xCurrent

    def locmin_value(self, left_x, right_x, m = min):
        quality = 1000
        h = (right_x - left_x) / quality
        return m([left_x + h*i for i in range(quality + 1)], key = lambda x: self.subst(x))

    def locmax_value(self, left_x, right_x):
        return self.locmin_value(left_x, right_x, m = max)

class QuadraticPolynomial (Polynomial):
    def __init__(self, koefficients):
        if Polynomial(koefficients).degree() > 2:
            try:
                raise (DegreesToBig(Polynomial(koefficients).degree()))
            except DegreesToBig as error:
                print(error)
        else:
            Polynomial.__init__(self, koefficients)

    def __mul__(self, other):
        result = Polynomial.__mul__(self, other)
        if result.degree() > 2:
            try:
                raise (DegreesToBig(result.degree()))
            except DegreesToBig as error:
                print(error)
        else:
            return result

    def __pow__(self, power, modulo=None):
        self = Polynomial(self.koefficients)
        result = Polynomial.__pow__(self, power, modulo)
        if result.degree() > 2:
            try:
                raise (DegreesToBig(result.degree()))
            except DegreesToBig as error:
                print(error)
        else:
            return result

    def solve(self):
        a = self.koefficients[2]
        b = self.koefficients[1]
        c = self.koefficients[0]
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return []
        elif discriminant > 0:
            return [(-b - sqrt(discriminant)) / (2 * a), (-b + sqrt(discriminant)) / (2 * a)]
        else:
            return [-b/2/a]

class DegreesToBig(Exception):
    def __init__(self, x, d = 2):
        self.x = x
        self.d = d

    def __str__(self):
        return ("В результате операции получился многочлен степени {}, максимально допустимая степень {}.".format(self.x, self.d))


a = Polynomial([-1, 0, 1])
b = Polynomial([1, 2, 1])
c = QuadraticPolynomial([-1, 0, 1])
print(Polynomial([0,4]) + Polynomial([0,-4]) == Polynomial([0]))
print(Polynomial(4))