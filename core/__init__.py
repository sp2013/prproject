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
    imagepath = '/home/priyal/Pictures/test/apples.jpg'

    image = cv2.imread(imagepath, cv2.IMREAD_COLOR)
    croppedimage = cropimage(imagepath, left, top, right, bottom)
    gray_image = clrtogray(imagepath)
    hsv_image = clrtohsv(imagepath)

    # DISPLAY image
    # Create a window for display.
    cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("cropped image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("gray image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("hsv image", cv2.WINDOW_NORMAL)

    cv2.imshow("input image", image)
    cv2.imshow("cropped image", croppedimage)
    cv2.imshow("gray image", gray_image)
    cv2.imshow("hsv image", hsv_image)

    cv2.waitKey(0)  # Wait for a keystroke in the window

    cv2.destroyAllWindows()
