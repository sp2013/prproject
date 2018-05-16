# Import numpy
import numpy as np
import cv2


'''
    shows different ways of creating numpy arrays.
'''
def createarrays():

    # Create a 1 dimensional array
    arr = np.array([5, 10, 15])
    # To print the data type.
    print (arr.dtype)
    # Prints int64
    # To print the shape of the array.
    print (arr.shape)
    # Prints "(3,)"
    # Accessing the values stored and printing them.
    print (arr[0], arr[1], arr[2])
    # Prints "5 10 15"
    # Values of the array can be directly changed
    arr[2] = 35
    # To print the whole array.
    print (arr)
    # Prints "[5, 10, 35]"
    # Create a 2 dimensional array
    twoArr = np.array([[5,10],[15,20],[25,30]])
    # To print the shape of the array.
    print (twoArr.shape)
    # Prints "(3,2)"
    # Accessing the values stored and printing them.
    print (twoArr[0, 0], twoArr[0, 1], twoArr[1, 0])
    # Prints "5 10 15"
    # To print the whole array.
    print (twoArr)
    # Prints "[[ 5 10], [15 20],  [25 30]]"
    return


'''
    display width, height, channels of numpy array.
'''
def displayattributes():
    # Load a color image in BGR
    img = cv2.imread('/home/priyal/Pictures/test/apples.jpg', 1)
    # Find the number of rows in the image
    imgRows = img.shape[0]
    # Find the number of columns in the image
    imgCols = img.shape[1]
    # Find the number of channels in the image
    Channels = img.shape[2]
    #msg = 'image width: ' + imgCols + '\nimage height: ' + imgRows + '\nimage channels: ' + Channels
    print('image width: ', imgCols,'\nimage height: ', imgRows, '\nimage channels: ', Channels)