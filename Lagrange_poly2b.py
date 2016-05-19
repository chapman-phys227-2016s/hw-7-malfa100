"""
File: Lagrange_poly2b.py
Exercise 5.25
Copyright (c) 2016 Andrew Malfavon
License: MIT
Investigate the behavior of Lagrange's interpolating polynomials.
"""

import Lagrange_poly2 as p1
import numpy as np
import matplotlib.pyplot as plt

#Graph for n = 2, 4, 6, and 10
def graph1():
    n = [2, 4, 6, 10]
    p1.graph2(np.abs, n, -2, 2)
    plt.title('f(x) = |x| and Interpolation Points')
    plt.xlim(-2.0, 2.0)
    plt.ylim(0.0, 2.1)

#graph for n = 13, and 20
def graph2():
    n = [13, 20]
    p1.graph2(np.abs, n, -2, 2)
    plt.title('f(x) = |x| and Interpolation Points')
    plt.xlim(-2.0, 2.0)
    plt.ylim(-4.5, 5.5)