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

def computeHOGFeatures(directoryPath):

    HOG_Width = 64
    HOG_Height = 128
    HOG_FeatureCount = 3780

    posSamplesFolder = directoryPath + '/pos'
    negSamplesFolder = directoryPath + '/neg'
    annotationsFolder = directoryPath + '/annotations'
    Label = 1 # for presence of human, Label is 1.
    imageCount = 0
    totalImages = 0 # number of positive plus negative samples.
    for root, dirs, files in os.walk(posSamplesFolder):
        totalImages = len(files)

    for root, dirs, files in os.walk(negSamplesFolder):
        totalImages = totalImages + len(files)

    # allocate HOG features array for totalImages
    HOGFeaturesArray = np.zeros(shape=(totalImages, HOG_FeatureCount))
    LabelsArray = np.zeros(shape=(totalImages, 1))

    # ---------------- FEATURE  COMPUTATION LOOP FOR POSITIVE SAMPLES ----------------
    for root, dirs, files in os.walk(posSamplesFolder):
        left = 0
        top = 0
        right = 0
        bottom = 0

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
                boundingboxImage = image[top:bottom, left:right] #crop as per bounding box
                #cv.imshow("Human", boundingboxImage)
                #cv.waitKey(0)
                #cv.destroyAllWindows()
                # resize cropped bounding box containing human figure to 64 x 128
                scaleX = HOG_Width / boundingboxImage.shape[1]
                scaleY = HOG_Height / boundingboxImage.shape[0]
                scaledBoxImg = cv.resize(boundingboxImage, None, fx=scaleX, fy=scaleY, interpolation=cv.INTER_LINEAR)
                hog = cv.HOGDescriptor()
                HOGFeaturesArray[imageCount] = (hog.compute(scaledBoxImg)).ravel()
                LabelsArray[imageCount][0] = Label  # assign label
                imageCount = imageCount + 1
                msg = 'Processed ' + imageCount.__str__() + ' of ' + totalImages.__str__()
                print(msg)

    # ---------------- FEATURE  COMPUTATION LOOP FOR NEGATIVE SAMPLES ----------------
    for root, dirs, files in os.walk(negSamplesFolder):
        Label = 0  #change Label value to 0, for negative samples.
        # get all image names from 'files' list in loop
        for name in files:
            extn = name.split(".")[-1]
            if extn == 'png':  # look for image with png extension.
                negImagePath = negSamplesFolder + '/' + name
                image = cv.imread(negImagePath)
                # cv.imshow("Human", image)
                # cv.waitKey(0)
                # cv.destroyAllWindows()
                # resize image bounding box to 64 x 128
                scaleX = HOG_Width / image.shape[1]
                scaleY = HOG_Height / image.shape[0]
                scaledBoxImg = cv.resize(image, None, fx=scaleX, fy=scaleY, interpolation=cv.INTER_LINEAR)
                hog = cv.HOGDescriptor()
                HOGFeaturesArray[imageCount] = (hog.compute(scaledBoxImg)).ravel() # convert tall vector to horizontal with ravel()
                LabelsArray[imageCount][0] = Label  # assign label
                imageCount = imageCount + 1
                msg = 'Processed ' + imageCount.__str__() + ' of ' + totalImages.__str__()
                print(msg)

    featuresFile = directoryPath + '/features.csv'
    labelsFile = directoryPath + '/labels.csv'
    np.savetxt(featuresFile, HOGFeaturesArray, fmt='%1.4f', delimiter=',')
    np.savetxt(labelsFile, LabelsArray, fmt='%d')



