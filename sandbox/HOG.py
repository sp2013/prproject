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

    # mag and angle have three channels each. pick up max value of gradient and corresponding angle to convert
    # this to array with only one channel.
    width = mag.shape[1]
    height = mag.shape[0]

    gradient1D = np.array(width, height, dtype = np.float)
    angle1D = np.array(width, height, dtype=np.float)

    for rows in range(0, height):
        for cols in range(0, width):
            maxgrad = np.maximum(mag[][])




    # wrap around angle values beyond 180 - 360 to 0 - 180


    # compute histogram of gradients

    # divide image in to blocks of 8 x 8

    xblocks = (int)(width / 8)
    yblocks = (int)(height / 8)

    counter = 0
    for x_outer in range (0, xblocks-1): # loop from 0 - 6 ...total 7
        for y_outer in range(0, yblocks-1): # loop from 0 - 14 ... total 15
            x_start = x_outer
            x_end = x_start + 2
            y_start = y_outer
            y_end = y_start + 2
            for x_inner in range(x_start, x_end):
                for y_inner in range(y_start, y_end): # four blocks of 8 x 8 for every block
                    left = x_inner*8
                    top = y_inner*8
                    right = left + 8
                    bottom = top + 8
                    print("{}: {}-{}, {}-{}".format(counter, left, top, right, bottom))  # display image dimensions.
                    counter = counter + 1
                    hist = computehistogram(angle[left:right, top:bottom], mag[left:right, top:bottom]) # hist is 1x9 vector


    # for each block, compute histogram using angle bins.


getHOG('../testData/juggballs.jpg')
print('done')

