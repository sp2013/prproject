'''
    SVM.py
'''
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
import pickle # for loading and saving model files
import matplotlib.pyplot as plt
from numpy import genfromtxt

def train(trainingDataFolder, featureFile, labelFile):

    y_train1 = genfromtxt(labelFile)
    y_train = np.zeros(y_train1.shape, dtype=np.int32)
    for items in range(y_train1.shape[0]):
        y_train[items] = y_train1[items]
    x_train = genfromtxt(featureFile, delimiter=',')


    # Create a svm Classifier
    clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)  # Linear Kernel

    # Train the model using the training sets
    clf.fit(x_train, y_train)

    # Save model file
    modelFile = trainingDataFolder + '/SVMModel.bin'
    pickle.dump(clf, open(modelFile, 'wb'))

    return modelFile


def test(modelFile, featuresFile):

    model = pickle.load(open(modelFile, 'rb'));
    x_test = genfromtxt(featuresFile, delimiter=',')

    # Create a svm Classifier
    clf = svm.SVC(kernel='linear')  # Linear Kernel

    # Predict the response for test dataset
    y_pred = clf.predict(x_test)

    return y_pred



def printfeatureslabels():

    # load dataset
    cancer = datasets.load_breast_cancer()
    print("Features:", cancer.feature_names)
    print("Labels:", cancer.target_names)
    print("Data size: ", cancer.data.shape) # 569 x 30. attributes x features
    print(cancer.data[0:5])
    # Split dataset into training set and test set..# 70% training and 30% test
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=109)

    # Create a svm Classifier
    clf = svm.SVC(kernel='linear')  # Linear Kernel

    # Train the model using the training sets
    clf.fit(X_train, y_train)

    # Save model file
    modelfile = 'C:/Users/patils7/Documents/SVM/model1.bin'
    pickle.dump(clf, open(modelfile, 'wb'))

    readModel = pickle.load(open(modelfile, 'rb'));

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    print('success')