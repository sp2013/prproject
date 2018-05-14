import cv2
import numpy as np
from matplotlib import pyplot as plt


'''
    function to crop image as per input coordinates.
    return cropped image to the caller.
'''
def cropimage(srcimage, left, top, right, bottom):

    image = cv2.imread(srcimage)
    croppedimage = image[top:bottom, left:right]
    return croppedimage
