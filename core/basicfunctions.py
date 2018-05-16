import cv2
import numpy as np
from matplotlib import pyplot as plt


'''
    function to crop image as per input coordinates.
    return cropped image to the caller.
'''
def cropimage(srcimage, left, top, right, bottom):

    image = cv2.imread(srcimage, cv2.IMREAD_COLOR)
    if image is None:
        print("Can not open or find the image.")
    croppedimage = image[top:bottom, left:right]
    return croppedimage


'''
    convert color input image to gray
'''
def clrtogray(image):

    image = cv2.imread(image, cv2.IMREAD_COLOR)
    if image is None:
        print("Can not open or find the image.")
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # cv2.imwrite('/home/priyal/Pictures/output/apples.jpg', gray_image)
    return gray_image


'''
    convert rgb color image to hsv
'''
def clrtohsv(image):
    image = cv2.imread(image)
    hsvimage = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    return hsvimage

