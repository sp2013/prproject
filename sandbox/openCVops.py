import cv2
import numpy as np
from matplotlib import pyplot as plt

''' 
    this function shows how to read image in to numpy array 
    and display it using matplotlib.
    also shows how to modify numpy array contents.
'''
def dispNumpyArrayAsImage(image):

    imgArray = cv2.imread(image)
    imgArray[0:100, 0:100] = (255, 0, 0)
    plt.imshow(imgArray, interpolation='nearest')
    plt.show()
    return

def addRedSquareAtCenter(image)
    