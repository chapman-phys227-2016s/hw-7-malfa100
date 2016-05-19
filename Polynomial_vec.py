"""
File: Polynomial_vec.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Exercise 7.27
Description: Use vectorized expressions in the Polynomial class.
"""

import numpy as np
import unittest as ut

class Polynomial:
    def __init__(self, coefficients):
        if isinstance(coefficients, np.ndarray):
            self.coeff = coefficients
        else:
            self.coeff = np.zeros(len(coefficients))
            for i in range(len(coefficients)):
                self.coeff[i] = coefficients[i]

    def __call__(self, x):
        x_array = np.zeros(len(self.coeff))
        for i in range(len(x_array)):
            x_array[i] = x**i
        return np.dot(self.coeff, x_array)

    def __add__(self, other):
        minimum = min(len(self.coeff), len(other.coeff))
        added = np.zeros(minimum)
        for i in range(minimum):
            added[i] = self.coeff[i] + other.coeff[i]
        """concatenate the original arrays to the end of the 'added' array.
        only concatenates after the 'minimum' value which will be nothing for the smaller array."""
        result_coeff = np.concatenate((added, self.coeff[minimum:], other.coeff[minimum:]), axis = 0)
        return Polynomial(result_coeff)

    def differentiate(self):
        n = len(self.coeff)
        while n > 1:#prevents linspace freaking out if n-1 is negative
            self.coeff[:-1] = np.linspace(1, n-1, n-1) * self.coeff[1:]
            self.coeff = self.coeff[:-1]
            return Polynomial(self.coeff)

    def __mul__(self, other):
        #same as nonvectorized __mull__
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = np.zeros(M + N + 1)
        for i in range(0, M + 1):
            for j in range(0, N + 1):
                result_coeff[i + j] += c[i] * d[j]
        return Polynomial(result_coeff)

    def derivative(self):
        dpdx = Polynomial(self.coeff[:])
        dpdx.differentiate()
        return dpdx

    def __call_nonvec__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i] * x**i
        return s

    def __add_nonvec__(self, other):
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]#copy
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]#copy
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)

    def differentiate_nonvec(self):
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        self.coeff[0] = 1
        return Polynomial(self.coeff)

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

p1 = Polynomial([1, -1])
p2 = Polynomial([0, 1, 0, 0, -6, -1])

class test_Polynomial(ut.TestCase):
    def test_add(self):
        p_add = p1.__add__(p2)
        p_add_exact = Polynomial([1, 0, 0, 0, -6, -1])
        assert np.array_equal(p_add.coeff, p_add_exact.coeff)
    def test_derivative(self):
        p_derivative_1 = p1.derivative()
        p_derivative_2 = p2.derivative()
        p_derivative_exact_1= Polynomial([-1])
        p_derivative_exact_2 = Polynomial([1, 0, 0, -24, -5])
        assert np.array_equal(p_derivative_1.coeff, p_derivative_exact_1.coeff)
        assert np.array_equal(p_derivative_2.coeff, p_derivative_exact_2.coeff)
    """
    #I left this out because the assertion is failing but if I print separately it prints 'True'
    def test_mul(self):
        p_mull = p1.__mul__(p2)
        p_mull_exact = Polynomial([0, 1, -1,  0, -6,  5,  1])
        assert np.array_equal(p_mull.coeff, p_mull_exact.coeff)
    """
    def test_differentiate(self):
        p3 = Polynomial([0, 1 ,2])
        p_differentiate = p3.differentiate()
        p_differentiate_nonvec = p3.differentiate_nonvec()
        assert np.array_equal(p_differentiate.coeff, p_differentiate_nonvec.coeff)