"""
File: Lagrange_poly2.py
Exercise 5.24
Copyright (c) 2016 Andrew Malfavon
License: MIT
Plot Lagrange's interpolating function
"""

import numpy as np
import Lagrange_poly1 as p1
import matplotlib.pyplot as plt

#Takes in a function and a number of interpolation poits along with p_L(x) from the previous exercise
def graph(f, n, xmin, xmax, resolution=1001):
    x_values = np.linspace(xmin, xmax, n)
    y_values = f(x_values)
    x_arr = np.linspace(xmin, xmax, resolution)
    y_arr = []
    for x in x_arr:
        y_arr.append(p1.p_L(x, x_values, y_values))
    plt.plot(x_values, y_values, 'ko')
    plt.plot(x_arr, y_arr)
    plt.title('Interpolation Polynomial and sin(x) from 0 to pi')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-0.1, 3.2)
    plt.ylim(-0.1, 1.1)

#Used in exercise 5.25. Allows n to be an array.
def graph2(f, n, xmin, xmax, resolution=1001):
    for i in n:
        x_values = np.linspace(xmin, xmax, i)
        y_values = f(x_values)
        x_arr = np.linspace(xmin, xmax, resolution)
        y_arr = []
        for x in x_arr:
            y_arr.append(p1.p_L(x, x_values, y_values))
        plt.plot(x_values, y_values, 'ko')
        plt.plot(x_arr, y_arr)
    plt.title('Interpolation Polynomial and sin(x) from 0 to pi')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-0.1, 3.2)
    plt.ylim(-0.1, 1.1)