"""
File: Lagrange_poly4.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Exercise 7.9
Description: Use a constructor to accept a function f(x) for computing the interpolation points.
"""

import numpy as np
import Lagrange_poly2 as LP2
import unittest as ut

class LagrangeInterpolation():
    #constructor based on suggestions from book
    def __init__(self, arg1, arg2, arg3):
        #first possible set of arguments:
        if (isinstance(arg1, np.ndarray)) and (isinstance(arg2, np.ndarray)):
            self.xp = arg1
            self.yp = arg2
        #second possible set of arguments:
        elif (callable(arg1) is True) and (isinstance(arg2, (list,tuple))) and (isinstance(arg3, int)):
            self.f = arg1
            self.x = arg2
            self.n = arg3
            self.xp = np.linspace(arg2[0], arg2[1], arg3)
            self.yp = (arg1(self.xp))
        else:
            print "Invalid parameters."

    def __call__(self, x):
        return LP2.p1.p_L(x, self.xp, self.yp)

    def plot(self):
        LP2.graph(self.f, self.n, self.x[0], self.x[-1])


class test(ut.TestCase):
    def test_p_L(self):
        myfunction = np.sin
        x = [0, np.pi]
        n = 11
        p_L = LagrangeInterpolation(myfunction, x, n)
        LP2.p1.test_p_L(p_L.xp, p_L.yp)