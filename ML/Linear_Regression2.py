'''
    Linear_Regression2.py
    Implements Gradient Descent Algorithm
'''
import numpy as np
import random
import matplotlib.pyplot as plt

def linear_regression2():
    '''
        1. Read training data in to input, output array.
        2. Initialize theta0 - y intercept, theta1 - slope of line.
        3. Repeat following steps until convergence:
            a. Compute theta0.
            b. Compute theta1.
            c. Compute cost.
            d. Check convergence by finding the difference between previous and current cost.
        4. Plot data with line using theta0, theta1.
    '''
    x = np.array([10, 9, 2, 15, 10, 16, 11, 16])
    y = np.array([95, 80, 10, 50, 45, 98, 38, 93])
    m = x.size
    theta0 = random.random()
    theta1 = random.random()
    delta = 1000000;
    error = 0.05
    learningrate = 0.001

    prevJtheta = 1000
    Jtheta = 1000

    while (delta > error):
        # compute theta0
        hx = theta0 + theta1*x
        s1 = (hx - y).sum() / m
        temp0 = theta0 - learningrate * s1

        # compute theta1
        s2 = ((hx - y) * x).sum() / m
        temp1 = theta1 - learningrate * s2

        theta0 = temp0
        theta1 = temp1

        #compute cost
        hx = theta0 + theta1 * x
        tempx = (hx - y) * (hx - y)
        Jtheta = tempx.sum() / (2 * m)

        delta = abs(prevJtheta - Jtheta)
        prevJtheta = Jtheta

    plt.xlabel('X')
    plt.ylabel('Y')
    axis = plt.axis([0, 20, 0, 100])
    plt.grid(True)
    plt.plot(x, y, 'k.')
    plt.plot(x, theta1*x + theta0, '-')
    plt.show()

    return theta0, theta1


