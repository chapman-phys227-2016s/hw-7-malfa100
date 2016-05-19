"""
File: Lagrange_poly3.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Exercise 7.8
Description: Use a class to implement Lagrange's interpolation method.
"""

import numpy as np
import Lagrange_poly2 as LP2
import unittest as ut#used in test.

class LagrangeInterpolation():
    def __init__(self, xarray, yarray):
        self.xp = xarray
        self.yp = yarray

    def __call__(self, x):
        return LP2.p1.p_L(x, self.xp, self.yp)

    def plot(self):
        LP2.graph(np.sin, 5, 0, np.pi)

class test(ut.TestCase):
    def test_p_L(self, xp = np.linspace(0, np.pi, 5), yp = np.sin(np.linspace(0, np.pi, 5))):
        LP2.p1.test_p_L(xp, yp)