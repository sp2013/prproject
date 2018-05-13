import cv2
import numpy as np
from matplotlib import pyplot as plt

''' 
    this function shows how to read image in to numpy array 
    and display it using matplotlib.
    also shows how to modify numpy array contents.
    OpenCV represents RGB images as multi-dimensional NumPy arrays…but in reverse order!
'''


def displaynumpyarray(image):

    imgarray = cv2.imread(image)
    plt.imshow(cv2.cvtColor(imgarray, cv2.COLOR_BGR2RGB))
    plt.show()
    return

'''
    this function adds square of input color size 200x200 symmetrically at the center.
'''
def addsquareatcenter(image, clr):
    imgarray = cv2.imread(image)
    print("Image shape: %d x %d", imgarray.shape[0], imgarray.shape[1])
    centerx = imgarray.shape[0]/2
    centery = imgarray.shape[1]/2
    imgarray[(int)(centerx-100):(int)(centerx+100), (int)(centery-100):(int)(centery+100)] = clr
    plt.imshow(cv2.cvtColor(imgarray, cv2.COLOR_BGR2RGB))
    plt.show()
    return


'''
    this function adds horizontal stripes of input color 
'''
def addghorzstripes(image, clr):
    imgarray = cv2.imread(image)
    print("Image shape: %d x %d", imgarray.shape[0], imgarray.shape[1])
    stripescount = 3
    bandheight = (int)(imgarray.shape[1] / (2*stripescount))
    for stripe in range(0, stripescount):
        imgarray[2*stripe*bandheight:2*stripe*bandheight+bandheight, ] = clr # for band of rows with all columns
    plt.imshow(cv2.cvtColor(imgarray, cv2.COLOR_BGR2RGB))
    plt.show()
    return


'''
    this function adds vertical stripes of input color 
'''
def addgvertstripes(image, clr):
    imgarray = cv2.imread(image)
    print("Image shape: %d x %d", imgarray.shape[0], imgarray.shape[1])
    stripescount = 3
    bandwidth = (int)(imgarray.shape[0] / (2*stripescount))
    for stripe in range(0, stripescount):
        imgarray[ :, 2*stripe*bandwidth:2*stripe*bandwidth+bandwidth] = clr # for band of rows with all columns
    plt.imshow(cv2.cvtColor(imgarray, cv2.COLOR_BGR2RGB))
    plt.show()
    return


'''
    this functions shows different ways of creating array and some arithmentic operations
    on it.
'''
def createnparrays():
    x = np.array([[1,2], [3,4]], dtype=np.float64)
    y = np.array([[5,6], [7,8]], dtype=np.float64)

    #display sum of arrays.
    print(x + y)
    print("other way of adding array")
    print(np.add(x, y))
    print(np.sqrt(x))


