import numpy as np
from matplotlib import pyplot as plt
import cv2

def grayhistogram(imagepath):

    image = cv2.imread(imagepath, cv2.IMREAD_UNCHANGED)
    if image is None:
        print("Can not open or find the image.")
        return

    cv2.imshow("Original", image)
    cv2.waitKey(0)

    # compute histogram
    hist = cv2.calcHist([image], [0], None, [256], [0, 256]) # image, channel no., mask, bins, range

    # plot
    plt.figure()
    plt.title("Gray Histogram")
    plt.xlabel("Bins")
    plt.ylabel(("# of pixels"))
    plt.plot(hist)
    plt.xlim(0, 256)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


def colorhistogram(imagepath):

    image = cv2.imread(imagepath)
    if image is None:
        print("Can not open or find the image.")
        return

    cv2.imshow("Original", image)
    cv2.waitKey(0)

    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title("’Flattened’ Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    # compute histogram for all channels.
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    # plot
    plt.plot(hist)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


'''
    Histogram equalization:
    This method is useful when an image contains foregroun-
    ds and backgrounds that are both dark or both light. It
    tends to produce unrealistic effects in photographs; how-
    ever, it is normally useful when enhancing the contrast of
    medical or satellite images.
'''
def histoequalize(imagepath):

    image = cv2.imread(imagepath, cv2.IMREAD_UNCHANGED)
    if image is None:
        print("Can not open or find the image.")
        return

    eq = cv2.equalizeHist(image)

    cv2.imshow("Histogram equalization", np.hstack([image, eq]))
    cv2.waitKey(0)
    return