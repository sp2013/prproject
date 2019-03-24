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
from sklearn.metrics import classification_report,accuracy_score
from sklearn.externals import joblib

def train(trainingDataFolder):

    y_train = genfromtxt(labelFile)
    y_train1 = np.zeros(y_train.shape, dtype=np.int32)
    for items in range(y_train.shape[0]):
        y_train1[items] = y_train[items]
    x_train1 = genfromtxt(featureFile, delimiter=',')

    # Create a svm Classifier
    # clf = svm.SVC(kernel='linear')  # Linear Kernel
    clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=1, gamma='auto', kernel='linear',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.0001, verbose=False)

    X_train, X_test, y_train, y_test = train_test_split(x_train1, y_train1, test_size=0.3, random_state=109)

    clf.fit(x_train1, y_train1)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    y_pred1 = clf.predict(x_train1)
    accuracy = accuracy_score(y_train1, y_pred1)

    featuresTestfile = trainingDataFolder + '/featuresTest.csv'
    x_test = genfromtxt(featuresTestfile, delimiter=',')
    y_pred = np.zeros(x_test.shape[0], dtype=np.int32)

    # Predict the response for test dataset
    y_pred = clf.predict(x_test)

    # Save model file
    modelFile = trainingDataFolder + '/SVMModel.bin'
    pickle.dump(clf, open(modelFile, 'wb'))
    pickle.close()

    modelFile1 = trainingDataFolder + '/SVMModel1.bin'
    joblib.dump(clf, open(modelFile1, 'wb'))

    return modelFile1


def test(modelFile, featuresFile, labelFile):

    y_read = genfromtxt(labelFile)
    y_test = np.zeros(y_read.shape, dtype=np.int32)
    for items in range(y_read.shape[0]):
        y_test[items] = y_read[items]
    x_test = genfromtxt(featuresFile, delimiter=',')

    model = pickle.load(open(modelFile, 'rb'));

    # Predict the response for test dataset
    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)

    return accuracy


