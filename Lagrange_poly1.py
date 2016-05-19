"""
File: Lagrange_poly1.py
Exercise 5.23
Copyright (c) 2016 Andrew Malfavon
License: MIT
Implement Lagrange's interpolation formula
for a coninuous function.
"""

import numpy as np

#multiples each result of the array
def L_k(x, k, xp, yp):
    xk = xp[k]
    xp = np.delete(xp, k)
    arr = []
    for i in range(len(xp)):
        arr.append((x - xp[i]) / (xk - xp[i]))
    return np.prod(arr)

#sums each result of the array
def p_L(x, xp, yp):
    arr = []
    for k in range(len(xp)):
        arr.append(yp[k] * L_k(x, k, xp, yp))
    return np.sum(arr)

#tests the polynomial p_L goes through each point
def test_p_L(xp = np.linspace(0, np.pi, 5), yp = np.sin(np.linspace(0, np.pi, 5))):
    values = 0
    for k in range(len(xp)):
        values += abs(p_L(xp[k], xp, yp) - yp[k])
    return values
    assert values == 0.0