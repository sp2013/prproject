import numpy as np
from skimage import data
from skimage import io
from matplotlib import pyplot as plt


def fun1():
    print('this part is to be made part of a function')
    x = {1, 2, 3, 4, 5}
    y = {6, 7, 8}
    #x = np.zeros(4)
    print(x)


def displayImage(image):
    io.imshow(image)
    plt.show(image)



