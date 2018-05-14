'''
    Python package created for testing core imaging functions
    like color conversion, resizing, cropping etc.
'''
import cv2
from skimage import io
import numpy as np
from matplotlib import pyplot as plt
from basicfunctions import *


if __name__ == '__main__':

    left = 0
    top = 50
    right = 150
    bottom = 150
    croppedimage = cropimage('/home/priyal/Pictures/test/apples.jpg', left, top, right, bottom)
    plt.imshow(cv2.cvtColor(croppedimage, cv2.COLOR_BGR2RGB))
    plt.show()
