import numpy as np
import gradient as grad
import cv2

# compute histogram of gradients using magnitude and angle block.
def computehistogram(angleblock, magblock):
    cv2.imshow("Gradient Image", magblock)
    cv2.waitKey()
    return

def getHOG(imagepath):

    # get magnitude and angle image
    mag, angle = grad.computegradient(imagepath)
    # cv2.imshow("Gradient Image", mag)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # wrap around angle values beyond 180 - 360 to 0 - 180


    # compute histogram of gradients

    # divide image in to blocks of 8 x 8
    width = mag.shape[1]
    height = mag.shape[0]
    xblocks = (int)(width / 8)
    yblocks = (int)(height / 8)

    for rows in range (0, xblocks):
        for cols in range(0, yblocks):
            print(rows*8 + ' ' + cols*8 + ' ')
            print("\n")
            #hist = computehistogram(angle[rows*8:rows*8+8, cols*8:cols*8+8],
            #                        mag[rows*8:rows*8+8, cols*8:cols*8+8])


    # for each block, compute histogram using angle bins.

