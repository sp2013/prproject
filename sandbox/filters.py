import numpy as np
import cv2

def averaging(imgpath):

    image = cv2.imread(imgpath)
    blurred = np.hstack([
        cv2.blur(image, (3, 3)),
        cv2.blur(image, (5, 5)),
        cv2.blur(image, (15, 15))])
    cv2.imshow("Averaged", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


def GaussianSmooth(imgpath):

    image = cv2.imread(imgpath)
    blurred = np.hstack([
                cv2.GaussianBlur(image, (3, 3), 0),
                cv2.GaussianBlur(image, (7, 7), 0),
                cv2.GaussianBlur(image, (15, 15), 0)])
    cv2.imshow("Gaussian", blurred)
    cv2.waitKey(0)
    return


'''
    Median blurring is more effective at removing salt-and-
    pepper style noise from an image because each central pixel
    is always replaced with a pixel intensity that exists in the
    image.
'''
def MedianBlur(imgpath):
    image = cv2.imread(imgpath)
    blurred = np.hstack([
                cv2.medianBlur(image, 3),
                cv2.medianBlur(image, 7),
                cv2.medianBlur(image, 15)])
    cv2.imshow("Median", blurred)
    cv2.waitKey(0)
    return


'''
        In order to reduce noise while still maintaining edges, we
    can use bilateral blurring. Bilateral blurring does
    this using two Gaussian distributions.
    The first Gaussian function only considers spatial neigh-
    bors, that is, pixels that appear close together in the ( x, y )
    coordinate space of the image. The second Gaussian then
    models the pixel intensity of the neighborhood, ensuring
    that only pixels with similar intensity are included in the
    actual computation of the blur.
    Overall, this method is able to preserve edges of an im-
    age, while still reducing noise. The largest downside to this
    method is that it is considerably slower than its averaging,
    Gaussian, and median blurring counterparts.
'''
def BilateralBlur(imgpath):
    image = cv2.imread(imgpath)
    blurred = np.hstack([
                cv2.bilateralFilter(image, 5, 15, 15),
                cv2.bilateralFilter(image, 5, 21, 21),
                cv2.bilateralFilter(image, 5, 27, 27)])
    cv2.imshow("Median", blurred)
    cv2.waitKey(0)
    return
