import numpy as np
import cv2
from skimage import data

'''
    Simple threshold...threshold image as per threshold parameter
'''
def simplethreshold():

    image = data.coins()

    # apply Gaussian blurring before thresholding to suppress noise.
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    # thresholding parameters: input image, threshold value, max value, threshold method
    (T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)

    output = np.hstack([image, thresh])
    cv2.imshow("SimpleThresholding", output)
    cv2.waitKey(0)

    return

'''
    Adaptive thresholding, considers small neighbors of pixels
    and then finds an optimal threshold value T for each neigh-
    bor. This method allows us to handle cases where there
    may be dramatic ranges of pixel intensities and the optimal
    value of T changes for different parts of the image.
'''
def adaptivethreshold():

    image = data.coins()

    # apply Gaussian blurring before thresholding to suppress noise.
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # thresholding parameters: input image, threshold value, max value, threshold method
    # the last two parameters are neightbor hood size to use for computing threshold.
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

    output = np.hstack([image, thresh])
    cv2.imshow("AdaptiveThresholding", output)
    cv2.waitKey(0)

    thresh = cv2.adaptiveThreshold(blurred, 255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
    output = np.hstack([image, thresh])
    cv2.imshow("AdaptiveThresholding Gaussian", output)
    cv2.waitKey(0)

    return