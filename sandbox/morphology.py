import cv2
import numpy as np

def erode(image):

    img = cv2.imread(image)
    if img is None:
        print("Can not open or find the image.")

    kernel = np.ones((9,9), np.uint8)
    erode = cv2.erode(img, kernel, iterations=1)

    cv2.imshow("Input", img)
    cv2.imshow("Erode", erode)

    cv2.waitKey();
    cv2.destroyAllWindows()
    return


def dilate(image):

    img = cv2.imread(image)
    if img is None:
        print("Can not open or find the image.")

    kernel = np.ones((9,9), np.uint8)
    erode = cv2.dilate(img, kernel, iterations=1)

    cv2.imshow("Input", img)
    cv2.imshow("Dilate", erode)

    cv2.waitKey();
    cv2.destroyAllWindows()
    return


'''
    Opening is just another name of erosion followed by dilation. It is useful in removing noise.
    Here we first apply opening operation followed by thresholding to convert gray scale output
    of opening to binary.
'''
def open(image):

    img = cv2.imread(image)
    if img is None:
        print("Can not open or find the image.")

    kernel = np.ones((5, 5), np.uint8)
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    cv2.imshow("Input", img)
    #cv2.imshow("Open", open)

    # retval is the threshold value returned by threshold function. It is same as input threshold value
    # or in case of Otsu, it's the value computed by Otsu method.
    retval, thresholded = cv2.threshold(open, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Thresholded", thresholded)

    cv2.waitKey();
    cv2.destroyAllWindows()
    return


'''
    Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the 
    foreground objects, or small black points on the object.
'''
def close(image):

    img = cv2.imread(image)
    if img is None:
        print("Can not open or find the image.")

    kernel = np.ones((9, 9), np.uint8)
    close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("Input", img)
    cv2.imshow("Close", close)

    # retval is the threshold value returned by threshold function. It is same as input threshold value
    # or in case of Otsu, it's the value computed by Otsu method.
    #retval, thresholded = cv2.threshold(open, 127, 255, cv2.THRESH_BINARY)
    #cv2.imshow("Thresholded", thresholded)

    cv2.waitKey();
    cv2.destroyAllWindows()
    return

'''
    Note: 
    Structuring Element
    We manually created a structuring elements in the previous examples with help of Numpy. It is 
    rectangular shape. But in some cases, you may need elliptical/circular shaped kernels. So for 
    this purpose, OpenCV has a function, cv.getStructuringElement(). You just pass the shape and 
    size of the kernel, you get the desired kernel.
    for example,
    cv.getStructuringElement(cv.MORPH_RECT,(5,5)),
    cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)),
    cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
    
    Morphology operations can also be used for thinning, skeletonizing etc.
'''