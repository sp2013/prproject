from Linear_Regression1 import *
from Linear_Regression2 import *
from kNN_Algo import *
from kMeans_Clustering import *

import numpy as np

if __name__ == '__main__':

    #intercept, slope = linear_regression2()

    '''
        kMeans clustering
        p6cluster - point p6 belongs to which cluster.
        count2 - number of points around cluster2
        centroid1 - centroid of cluster 1
        centroid2 - centroid of cluster 2
    '''
    p6cluster, count2, centroid1, centroid2 = kmeansclustering()
    msg = "P6 belongs to: " + p6cluster + "Number of points in cluster2: " + "Centroid1: " + centroid1[0] + "," + centroid1[1] + "Centroid2: "  + centroid2[0] + "," + centroid2[1]
    print(msg)
    '''
        kNN Algorithm
        class 1 - positive
        class 2 - positive
    '''
    k = 3
    point = np.array([6,6]) # testpoint

    dotClass = kNN_algo(point, k)
    print("As per normall kNN algo, test point belongs to class: ", dotClass)


    dotClass = WeightedkNN_algo(point, k)
    print("As per weighted kNN algo, test point belongs to class: ", dotClass)

