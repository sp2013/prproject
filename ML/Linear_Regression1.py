'''
    Linear_Regression1.py
    Uses nparray polyfit
'''
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets
import matplotlib.pyplot as plt

def linear_regression1():

    x = np.array([5, 13, 34, 37, 56])
    y = np.array([7, 24, 28, 46, 50])
    plt.scatter(x, y, color='red')
    m, b, _, _, _ = np.polyfit(x, y, 1, full=True)

    plt.xlabel('X')
    plt.ylabel('Y')
    axis = plt.axis([0, 600, 0, 600])
    plt.grid(True)
    plt.plot(x, y, 'k.')
    plt.plot(x, m*x+b, '-')
    plt.show()
