import numpy as np
import cv2

import gradient as gradObj

binsize = 20
anglecentres = binsize * np.arange(9)

# compute histogram of gradients using magnitude and angle block.
def computehistogram(angle, mag, blocksize):
    #cv2.imshow("Gradient Image", magblock)
    #cv2.waitKey()
    # wrap around angle values beyond 180 - 360 to 0 - 180
    binsize = 20
    histobinscount = anglecentres.shape[0]
    hist = np.zeros(histobinscount)
    for rows in range(0, blocksize):
        for cols in range(0, blocksize):
            center1 = 0
            center2 = 0
            angleval = (int)(angle[rows, cols])
            magval = mag[rows, cols]
            if angleval == 360:
                angleval = 0
            elif angleval > 180:
                angleval = angleval - 180
            # a = divmod(angleval, binsize) # gives array a[quotient, remainder]
            q = int(angleval / binsize)
            r = angleval - binsize * q
            if(r == 0):
                hist[q] += magval
            else: # case of not a boundary value for angle
                if q == blocksize:
                    center1 = anglecentres[q]
                    center2 = 0
                else:
                    center1 = anglecentres[q]
                    center2 = anglecentres[q+1]
                # find distribution of angleval in two bins center1 and center2
                val1 = (float)((binsize - (magval - anglecentres[center1])) * magval) / 20.0
                val2 = (float)((binsize - (anglecentres[center2]-magval)) * magval) / 20.0
                hist[center1] += val1
                hist[center2] += val2
    return hist


def getHOG(imagepath):

    # get magnitude and angle image
    grad, angle = gradObj.computegradient(imagepath)
    #cv2.imshow("Gradient Image", grad)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

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
    blocksize = 8
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
                    blockhist = computehistogram(gradmax[left:right, top:bottom], anglemax[left:right, top:bottom], blocksize) # hist is 1x9 vector
                    if counter == 0:
                        hist = blockhist
                    else:
                        hist = np.append(hist, blockhist)
                    counter = counter + 1

            # normalize histogram of size 36.
            histnorm = hist / np.linalg.norm(hist)
            if blocks == 0:
                imagehisto = histnorm
            else:
                imagehisto = np.append(imagehisto, histnorm)

            blocks = blocks + 1

    return imagehisto

hog = getHOG('../testData/juggballs.jpg')
print('done')

