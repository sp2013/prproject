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