import cv2
import numpy as np


'''
    openCV function 'connectedComponents' description:
    computes the connected components labeled image of boolean image.
    image with 4 or 8 way connectivity - returns N, the total number of labels [0, N-1] 
    where 0 represents the background label. ltype specifies the output label image type, 
    an important consideration based on the total number of labels or alternatively the 
    total number of pixels in the source image.
    
    Parameters
    image:	        the 8-bit single-channel image to be labeled
    labels:	        destination labeled image
    connectivity:	8 or 4 for 8-way or 4-way connectivity respectively
    ltype:	        output image label type. Currently CV_32S and CV_16U are supported.
'''
def ccanalysis(image):

    img = cv2.imread(image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    labels = np.ones((img.shape[0], img.shape[1]), dtype=np.ushort)
    ret = cv2.connectedComponents(img_gray, labels)
    ''' Suhas: it seems ret structure is a tuple. ret[0] - has number of labels including background. and
        ret[1] is labelled image of size input image width x height, labels starting with 1 for detected 
        objects. label 0 is for background.
    '''
    print(ret[1].shape)
    return


'''
    Statistics output for each label, including the background label, see below for available statistics. 
    Statistics are accessed via stats[label, COLUMN] where available columns are defined below.
    cv2.CC_STAT_LEFT The leftmost (x) coordinate which is the inclusive start of the bounding box in the horizontal direction.
    cv2.CC_STAT_TOP The topmost (y) coordinate which is the inclusive start of the bounding box in the vertical direction.
    cv2.CC_STAT_WIDTH The horizontal size of the bounding box
    cv2.CC_STAT_HEIGHT The vertical size of the bounding box
    cv2.CC_STAT_AREA The total area (in pixels) of the connected component
    
    Centroids is a matrix with the x and y locations of each centroid. The row in this matrix corresponds 
    to the label number.
'''
def ccanalysiswithstats(image):

    img = cv2.imread(image)
    img_binary = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    buffer = np.ones((img.shape[0], img.shape[1]), dtype=np.ushort)
    output = cv2.connectedComponentsWithStats(img_binary, buffer)
    # Get the results
    # The first cell is the number of labels
    num_labels = output[0] - 1 # output[0] count includes background I guess :~ Suhas
    # The second cell is the label matrix
    labels = output[1]
    # The third cell is the stat matrix
    stats = output[2]
    # The fourth cell is the centroid matrix
    centroids = output[3]

    # print bounding box for each label. #0 is excluded as its background.
    for label in range(0, num_labels+1):
        # get bounding box
        left = stats[label][cv2.CC_STAT_LEFT]
        top = stats[label][cv2.CC_STAT_TOP]
        width = stats[label][cv2.CC_STAT_WIDTH]
        height = stats[label][cv2.CC_STAT_HEIGHT]
        # get label
        centroid = centroids[label]

        print('label:',label,'left:',left,'top:',top,'width:',width,'height:',height,'Centroid:',centroid)

    return