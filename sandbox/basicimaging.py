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
    cv2.destroyAllWindows()
    return


'''
    rotate image as per input angle
'''
def rotateimage(image, angle):

    src = cv2.imread(image)

    dims = src.shape # get image shape
    scale = 1

    # The getRotationMatrix2D function takes the following parameters:
    # Center: point about which rotation will occur
    # rotationAngle: angle by which rotation is occurring
    # Scale : an optional scaling factor

    rotationMatrix = cv2.getRotationMatrix2D((dims[1] / 2, dims[0] / 2), angle, scale)

    print(rotationMatrix)

    result = cv2.warpAffine(src, rotationMatrix, (dims[1], dims[0]))

    cv2.imshow("Input Image", src)
    cv2.imshow("Rotated Image", result)

    cv2.waitKey()
    cv2.destroyAllWindows()
    return


'''
    Draw different shapes on the image
'''
def drawshapes(image):

    input = cv2.imread(image)
    src = cv2.resize(input, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)

    # Draw a line
    imageLine = src.copy()
    cv2.line(imageLine, (322, 179), (400, 183), (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imshow("imageLine", imageLine)

    # Draw a circle
    imageCircle = src.copy()
    cv2.circle(imageCircle, (350, 200), 150, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imshow("imageCircle", imageCircle)

    # Draw an ellipse
    # IMP Note: Ellipse Centers and Axis lengths must be integers
    imageEllipse = src.copy()
    cv2.ellipse(imageEllipse, (360, 200), (100, 170), 45, 0, 360, (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.ellipse(imageEllipse, (360, 200), (100, 170), 135, 0, 360, (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
    cv2.imshow("ellipse", imageEllipse)

    # Draw a rectangle (thickness is a positive integer)
    imageRectangle = src.copy()
    cv2.rectangle(imageRectangle, (208, 55), (450, 355), (0, 255, 0), thickness=2, lineType=cv2.LINE_8)
    cv2.imshow("rectangle", imageRectangle)

    # Put text into image
    imageText = src.copy()
    cv2.putText(imageText, "Mark Zuckerberg", (205, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("text", imageText)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return





