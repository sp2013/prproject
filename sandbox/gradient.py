import numpy as np
import cv2

'''
    Sobel function parameters:
    src_gray: In our example, the input image. Here it is CV_8U
    grad_x/grad_y: The output image.
    ddepth: The depth of the output image. We set it to CV_16S to avoid overflow.
    x_order: The order of the derivative in x direction.
    y_order: The order of the derivative in y direction.
    scale, delta and BORDER_DEFAULT: We use default values.
'''

def computegradient(image):

    img = cv2.imread(image)
    img = np.float32(img) / 255.0

    # Calculate gradient
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)

    mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)

    return mag, angle


def cannyedgedetection(image):

    img = cv2.imread(image)
    edgeimg = cv2.Canny(img, 100, 200)
    cv2.imshow("Canny edge", edgeimg)
    cv2.waitKey()


