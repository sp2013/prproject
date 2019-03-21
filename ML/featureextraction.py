'''
    train.py - program to get list of files in the given directory.
    a. For positive sample folder:
        1. From the given directory, search images with extension 'png'
        2. From the associated annotation file in 'annotations' folder, get bounding box of human figure in that image.
        3. Compute HOG feature on bounding box.
        4. Store computed feature in one row in .csv file.
    b. For Negative samples folder:
        1. From the given directory, search images with extension 'png'
        2. Compute HOG feature on bounding box.
        3. Store computed feature in one row in .csv file.
'''
import os
import cv2 as cv
import numpy as np
from array import array

def extractAndSaveFeatures(directoryPath):

    HOG_Width = 64
    HOG_Height = 128
    HOG_FeatureCount = 3780
    # Feature extraction for positive samples folder.
    posSamplesFolder = directoryPath + '/pos'
    annotationsFolder = directoryPath + '/annotations'
    featuresFile = directoryPath + '/features.txt'

    for root, dirs, files in os.walk(posSamplesFolder):
        left = 0
        top = 0
        right = 0
        bottom = 0
        imageCount = 0;
        HOGFeaturesArray = np.zeros(shape=(len(files), HOG_FeatureCount))
        # get all image names from 'files' list in loop
        for name in files:
            extn = name.split(".")[-1]
            if extn == 'png': # look for image with png extension.
                # Get bounding box from the corresponding annotation file
                imageAntnFile = annotationsFolder + '/' + name.split(".")[0] + '.txt'
                file1 = open(imageAntnFile, 'r')
                lines = file1.readlines()
                # after reversing the line containing bounding box appears at index 1.
                # sample line containing bounding box info is given below:
                # 'Bounding box for object 1 "PASperson" (Xmin, Ymin) - (Xmax, Ymax) : (194, 127) - (413, 647)'
                lines.reverse()
                line1 = lines[1]
                lines2 = line1.split(':')
                y = lines2[1].split('-')
                a = y[0].split(',')
                b = a[0].split('(')
                left = (int)(b[1]) # get left coordinate of bounding box as int

                c = a[1].split(')')
                top = (int)(c[0]) # get top coordinate of bounding box as int

                a = y[1].split(',')
                b = a[0].split('(')
                right = (int)(b[1]) # get right coordinate of bounding box as int

                c = a[1].split(')')
                bottom = (int)(c[0]) # get bottom coordinate of bounding box as int

                posImagePath = posSamplesFolder + '/' + name
                image = cv.imread(posImagePath)
                boundingbox = image[top:bottom, left:right] #crop as per bounding box
                #cv.imshow("Human", boundingbox)
                #cv.waitKey(0)
                #cv.destroyAllWindows()
                # resize cropped bounding box to 64 x 128
                scaleX = HOG_Width / boundingbox.shape[1]
                scaleY = HOG_Height / boundingbox.shape[0]
                scaledBox = cv.resize(boundingbox, None, fx=scaleX, fy=scaleY, interpolation=cv.INTER_LINEAR)
                hog = cv.HOGDescriptor()
                HOGFeaturesArray[imageCount] = (hog.compute(scaledBox)).ravel()
                #np.save(featuresFile, h)
                imageCount = imageCount + 1

        np.savetxt(featuresFile, HOGFeaturesArray, fmt='%1.4f')



