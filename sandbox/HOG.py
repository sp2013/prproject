import numpy as np
import cv2

import gradient as gradObj

blocksize = 8 # basic block size used for HOG computation.
binsize = 20
histobinscount = 9
numfeatures = 3780
anglecentres = binsize * np.arange(histobinscount)

def computeValues(center1, center2, angle, mag):
    val1 = 0
    val2 = 0
    num = (center2 - angle) * mag
    val1 = (float(num/binsize))
    val2 = (float)(mag - val1)
    return val1, val2

# compute histogram of gradients using magnitude and angle block.
def computehistogram(mag, angle, blocksize):
    #cv2.imshow("Gradient Image", magblock)
    #cv2.waitKey()
    # wrap around angle values beyond 180 - 360 to 0 - 180
    hist = np.zeros(histobinscount)
    for rows in range(0, blocksize):
        for cols in range(0, blocksize):
            angleval = (int)(angle[rows, cols])
            magval = mag[rows, cols]
            if magval == 0:
                continue
            center1 = (int)(angleval/binsize) * binsize
            center2 = center1 + binsize
            val1, val2 = computeValues(center1, center2, angleval, magval)
            center = divmod(angleval, 180)
            angleval = center[1]
            q = int(angleval / binsize)
            r = angleval - binsize * q
            # find distribution of angleval in two bins center1 and center2
            q1 = q
            q2 = q + 1
            if q == blocksize: # case of not a boundary value for angle
                q2 = 0
            hist[q1] += val1
            hist[q2] += val2
    return hist


def getHOG(imagepath):

    # get magnitude and angle image
    grad, angle = gradObj.computegradient(imagepath)
    #cv2.imshow("Gradient Image", grad)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    #cv2.imwrite('C:\\Output\\testFlowerGrad.bmp', grad)
    # mag and angle have three channels each. pick up max value of gradient and corresponding angle to convert
    # this to array with only one channel.
    height, width, bytesperpix = grad.shape

    gradmax = np.amax(grad, axis=2)
    gradmaxIndex = grad.argmax(axis=2)
    #cv2.imshow("max gradient", gradmax[:,:])
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    # create anglemax matrix that holds angle values corresponding to the maximum gradient.
    anglemax = np.zeros(shape=(height, width), dtype=np.float32)
    for rows in range(0, height):
        for cols in range(0, width):
            anglemax[rows, cols] = angle[rows, cols, gradmaxIndex[rows, cols]]

    # divide image in to blocks of 8 x 8
    xblocks = (int)(width / blocksize)
    yblocks = (int)(height / blocksize)
    blocks = 0
    imagehisto = []

    for x_outer in range (0, xblocks-1): # loop from 0 - 6 ...total 7

        for y_outer in range(0, yblocks-1): # loop from 0 - 14 ... total 15

            x_start = x_outer
            x_end = x_start + 2
            y_start = y_outer
            y_end = y_start + 2

            # loop for histogram of 16 x 16 block.
            counter = 0
            hist = []
            for x_inner in range(x_start, x_end):
                for y_inner in range(y_start, y_end): # four blocks of 8 x 8 for every block
                    left = x_inner*blocksize
                    top = y_inner*blocksize
                    right = left + blocksize
                    bottom = top + blocksize
                    print("{}: {}-{}, {}-{}".format(counter, left, top, right, bottom))  # display image dimensions.
                    blockhist = computehistogram(gradmax[top:bottom, left:right], anglemax[top:bottom, left:right], blocksize) # hist is 1x9 vector
                    if counter == 0:
                        hist = blockhist
                    else:
                        hist = np.append(hist, blockhist)
                    counter = counter + 1

            # normalize histogram of size 36.
            normdiv = 0.0001 + np.linalg.norm(hist) # to avoid divide by zero condition
            histnorm = hist / normdiv
            if blocks == 0:
                imagehisto = histnorm
            else:
                imagehisto = np.append(imagehisto, histnorm)

            blocks = blocks + 1

    return imagehisto

hogArray = np.zeros(shape=(4, numfeatures))
for x in range(0, 1):
    hogArray[x] = getHOG('..\\testData\\testFlower.png')

hog = cv2.HOGDescriptor()
im = cv2.imread('..\\testData\\testFlower.png')
h = hog.compute(im)
print('done')

