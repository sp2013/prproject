from featureextraction import *
from SVM import *

import os
import shutil

trainingDataFolder = 'C:/Users/patils7/Documents/SVM/INRIAPerson/Train'
modelFile = trainingDataFolder + '/SVMModel.bin'
featuresFile = trainingDataFolder + '/features.csv'
labelsFile = trainingDataFolder + '/labels.csv'
featuresTestFile = trainingDataFolder + '/featuresTest.csv'

def ComputeFeatures():
    # Compute HOG features and save to disk.
    featuresFile, labelsFile = computeHOGFeatures(trainingDataFolder)
    return

def Train():
    modelFile = train(trainingDataFolder, featuresFile, labelsFile)
    return

def Test():
    y_pred = test(modelFile, featuresTestFile)

if __name__ == '__main__':

    #ComputeFeatures()

    Train()

    Test()

    #printfeatureslabels()








'''
    file1 = open('C:/Users/patils7/Documents/SVM/INRIAPerson/Train/negList.txt', 'r')
    files = file1.readlines()
    dstn = 'C:/Users/patils7/Documents/SVM/INRIAPerson/Train/selected'
    for images in files:
        src = images.split('\n')[0]
        shutil.move(src, dstn)
'''




