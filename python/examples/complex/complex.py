#!/usr/bin/env python3


class SimpleComplex:
    _a = 0.0
    _b = 0.0


    def __init__(self, a=0.0, b=0.0):
        self._a = a
        self._b = b

    def __str__(self):
        return "{} + {}i".format(self._a, self._b)


    def __repr__(self):
        return str(self)


    @property
    def a(self):
        return self._a


    @a.setter
    def a(self, val):
        self._a = val


    @property
    def b(self):
        return self._b


    @b.setter
    def b(self, val):
        self._b = val


    def __add__(self, other):
        return SimpleComplex(self.a + other.a, self.b + other.b)


    def __mul__(self, other):
        return SimpleComplex(
                self.a * other.a - self.b * other.b,
                self.a * other.b - self.b * other.a,
                )

    def __or__(self, other):
        return NotImplemented


sc1= SimpleComplex()
sc2= SimpleComplex()
sc1.a = 2.3
sc2.b = 4.3

print(sc1, "*", sc2, "=", sc1*sc2)
print(sc1, "|", sc2, "=", sc1|sc2)
