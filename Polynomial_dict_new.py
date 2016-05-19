"""
File: Polynomial_dict_new.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Exercise 7.28
Description: Use a dictionary for the coeff attribute in the Polynomial class.
note: renamed because sage was not letting me save so I made a new file.
"""

import numpy as np
import copy

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        s = 0
        for k in range(len(self.coeff)):
            s += self.coeff[k] * x**k
        return s

    def __add__(self, other):
        result_coeff = self.coeff.copy()
        for k in other.coeff:
            if k in self.coeff:
                result_coeff[k] += other.coeff[k]
            else:
                result_coeff[k] = other.coeff[k]
        return Polynomial(result_coeff)

    def __mul__(self, other):
        result_coeff = {}
        for i in self.coeff:
            for j in other.coeff:
                if (i + j) in result_coeff:
                    result_coeff[i + j] += self.coeff[i] * other.coeff[j]
                else:
                    result_coeff[i + j] = self.coeff[i] * other.coeff[j]
        return Polynomial(result_coeff)

    def differentiate(self):
        n = len(self.coeff)
        self.coeff[:-1] = np.linspace(1, n-1, n-1) * self.coeff[1:]
        self.coeff = self.coeff[:-1]
        return Polynomial(self.coeff)

    def derivative(self):
        dpdx = Polynomial(self.coeff[:])
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s = ""
        for i in range(len(self.coeff)):
            if(self.coeff[i] != 0):
                s += " + %g*x^%d" % (self.coeff[i], i)
        s = s.replace("+ -", "- ")
        s = s.replace("x^0", "1")
        s = s.replace(" 1*", " ")
        s = s.replace("x^1 ", "x ")
        if s[0:3] == " + ":
            s = s[3:]
        if s[0:3] == " - ":
            s = "-" + s[3:]
        return s

def test():
    p1 = Polynomial({1:1, 100:-3})
    p2 = Polynomial({20:1, 1:-1, 100:4})
    p_add = (p1.__add__(p2))
    p_mull = (p1.__mul__(p2))
    assert p_add.coeff == {1:0, 100:1, 20:1}
    assert p_mull.coeff == {120: -3, 200: -12, 2: -1, 21: 1, 101: 7}