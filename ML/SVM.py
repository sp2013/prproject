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

def train(trainingDataFolder, featureFile, labelFile):

    y_train = genfromtxt(labelFile)
    y_train1 = np.zeros(y_train.shape, dtype=np.int32)
    for items in range(y_train.shape[0]):
        y_train1[items] = y_train[items]
    x_train1 = genfromtxt(featureFile, delimiter=',')

    # Create a svm Classifier
    # clf = svm.SVC(kernel='linear')  # Linear Kernel
    clf = svm.SVC(C=2.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=5, gamma='auto', kernel='linear',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.0001, verbose=False)

    X_train, X_test, y_train, y_test = train_test_split(x_train1, y_train1, test_size=0.3, random_state=109)

    clf.fit(x_train1, y_train1)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    featuresTestfile = trainingDataFolder + '/featuresTest.csv'
    x_test = genfromtxt(featuresTestfile, delimiter=',')
    y_pred = np.zeros(x_test.shape[0], dtype=np.int32)

    # Predict the response for test dataset
    y_pred = clf.predict(x_test)

    # Save model file
    modelFile = trainingDataFolder + '/SVMModel.bin'
    pickle.dump(clf, open(modelFile, 'wb'))

    return modelFile


def test(modelFile, featuresFile):

    model = pickle.load(open(modelFile, 'rb'));
    x_test = genfromtxt(featuresFile, delimiter=',')
    y_pred = np.zeros(x_test.shape[0], dtype=np.int32)

    # Predict the response for test dataset
    result = model.score(x_test, y_pred)

    return result



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