from featureextraction import *
from SVM import *

import os
import shutil

trainingDataFolder = 'C:/Users/patils7/Documents/SVM/SVM Assgn/100 leaves plant species'
modelFile = trainingDataFolder + '/SVMModel.bin'

def Train():
    modelFile = train(trainingDataFolder)
    return

def Test():
    accuracy = test(modelFile)

if __name__ == '__main__':

    Train()

    Test()










'''
    file1 = open('C:/Users/patils7/Documents/SVM/INRIAPerson/Train/negList.txt', 'r')
    files = file1.readlines()
    dstn = 'C:/Users/patils7/Documents/SVM/INRIAPerson/Train/selected'
    for images in files:
        src = images.split('\n')[0]
        shutil.move(src, dstn)
'''




