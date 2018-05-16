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


'''
    test crop and resizing.
'''
def cropresize(image):

    image = cv2.imread(image)

    # scaling factors.
    scalex = 0.4
    scaley = 0.4

    # Scaling Down the image 0.4 times
    scaledown = cv2.resize(image, None, fx=scalex, fy=scaley, interpolation=cv2.INTER_LINEAR)

    # Scaling up the image 4 times
    scaleup = cv2.resize(image, None, fx=scalex * 4, fy=scaley * 4, interpolation=cv2.INTER_LINEAR)

    # Cropped Image
    crop = image[0:150, 20:200]

    # Displaying all the images
    cv2.imshow("Original", image)
    cv2.imshow("Scaled Down", scaledown)
    cv2.imshow("Scaled Up", scaleup)
    cv2.imshow("Cropped Image", crop)

    cv2.waitKey(0)

    return

