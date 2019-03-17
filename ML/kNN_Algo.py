'''
    kNN_Algo.py
    Implements kNN algorithm
    1. Load the data
    2. Initialise the value of k
    3. For getting the predicted class, iterate from 1 to total number of training data points
        a. Calculate the distance between test data and each row of training data.
           Here we will use Euclidean distance as our distance metric since it’s the most popular method.
           The other metrics that can be used are Chebyshev, cosine, etc.
        b. Sort the calculated distances in ascending order based on distance values
        c. Get top k rows from the sorted array
        d. Get the most frequent class of these rows
    Return the predicted class
'''
import numpy as np
import random
import matplotlib.pyplot as plt

def sortfn(x):
    return np.sin(x[:, 0])

def kNN_algo(point, k):

    pos = np.array([[4,4],[6,2]])
    neg = np.array([[2,4],[4,2],[4,6],[6,4]])
    length = pos.shape[0] + neg.shape[0]
    dist = np.zeros((length, 2)) # two dimensional array, one for dist, other for class.
    count = 0
    for x in range(pos.shape[0]):
        pt = pos[x] - point[0]
        dist[count][0] = np.sqrt((pt*pt).sum())
        dist[count][1] = 0 # pos class indicator
        count = count + 1

    for x in range(neg.shape[0]):
        pt = neg[x] - point[0]
        dist[count][0] = np.sqrt((pt*pt).sum())
        dist[count][1] = 1 # neg class indicator
        count = count + 1

    predicate = sortfn(dist)
    sortedDistIndices = np.argsort(predicate)
    sortedDistIndices = sortedDistIndices[::-1]
    sortedDist = dist[sortedDistIndices]
    class1 = 0
    class2 = 0
    for i in range(k):
        if sortedDist[i][1] == 0:
            class1 = class1 + 1
        else:
            class2 = class2 + 1

    if class1 > class2:
        return 'positive'
    else:
        return 'negative'


def WeightedkNN_algo(point, k):

    pos = np.array([[4,4],[6,2]])
    neg = np.array([[2,4],[4,2],[4,6],[6,4]])
    length = pos.shape[0] + neg.shape[0]
    dist = np.zeros((length, 2)) # two dimensional array, one for dist, other for class.
    count = 0
    for x in range(pos.shape[0]):
        pt = pos[x] - point[0]
        dist[count][0] = 1 / (np.sqrt((pt*pt).sum())) # weight is reciprocal of distance. larger the distance, smaller the weight
        dist[count][1] = 0 # pos class indicator
        count = count + 1

    for x in range(neg.shape[0]):
        pt = neg[x] - point[0]
        dist[count][0] = 1 / (np.sqrt((pt*pt).sum())) # weight is reciprocal of distance. larger the distance, smaller the weight
        dist[count][1] = 1 # neg class indicator
        count = count + 1

    predicate = sortfn(dist)
    sortedWeightIndices = np.argsort(predicate)
    sortedWeight = dist[sortedWeightIndices]
    class1 = 0
    class2 = 0
    for i in range(k):
        if sortedWeight[i][1] == 0:
            class1 = class1 + 1
        else:
            class2 = class2 + 1

    if class1 > class2:
        return 'positive'
    else:
        return 'negative'




