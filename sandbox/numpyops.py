# Import numpy
import numpy as np
import cv2

appleimage = '/home/priyal/Pictures/test/apples.jpg'


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
    img = cv2.imread(appleimage, 1)
    # Find the number of rows in the image
    imgRows = img.shape[0]
    # Find the number of columns in the image
    imgCols = img.shape[1]
    # Find the number of channels in the image
    Channels = img.shape[2]
    #msg = 'image width: ' + imgCols + '\nimage height: ' + imgRows + '\nimage channels: ' + Channels
    print('image width: ', imgCols,'\nimage height: ', imgRows, '\nimage channels: ', Channels)
    return


'''
    create different types of numpy arrays like ones, zeros or I matrix.
'''
def createsomemorematrices():
    # Create an array of length 10 with all elements as 0
    a = np.zeros(10)
    # Prints "[ 0.  0.  0.  0.  0.]"
    print(a)
    # Create an array of length 10 of all ones
    a = np.ones(10)
    # Prints "[ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]"
    print(a)
    # Note for the functions above, specifying two dimensions (m,n) creates
    # a 2D numpy array of m rows and n columns
    # Create a 3x3 identity matrix
    a = np.eye(3)
    # Print out the matrix.Prints
    # "[[ 1.  0.  0.], [ 0.  1.  0.] ,[ 0.  0.  1.]]" (in separate lines)
    print(a)
    # For the above functions the return type is
    # float64 (can be found out by using a.dtype)
    # Forces the datatype to be int64 in place of float64
    a = np.ones(10, dtype=np.int64)
    # Print out the array.Prints "[1 1 1 1 1 1 1 1 1 1]"
    print(a)
    return


'''
    demonstrates how image types can be converted to different data types.
'''
def datatypesconversion():
    # Load an color image in BGR
    img = cv2.imread(appleimage, 1)
    # Prints uint8
    print(img.dtype)
    # Convert from uint8 to float32
    img = np.float32(img)
    # Prints float32
    print(img.dtype)
    # Convert from float32 to uint8
    img = np.uint8(img)
    # Prints uint8
    print(img.dtype)
    return
