'''
    kMeans_Clustering.py
    Steps:
    1. Select ‘c’ cluster centers.
    2. Calculate the distance between each data point and cluster centers.
    3. Assign the data point to the cluster center whose distance from the cluster center is minimum of all
       the cluster centers..
    4. Recalculate the new cluster center
    5. Recalculate the distance between each data point and new obtained cluster centers.
    6. If no data point was reassigned then stop, otherwise repeat from step 3).
'''
import numpy as np
import matplotlib.pyplot as plt

def kmeansclustering():

    dataPoints = np.array([[0.1, 0.6],[0.15, 0.71],[0.08, 0.9],[0.16, 0.85],[0.2, 0.3],[0.25, 0.5],
                           [0.24, 0.1],[0.3, 0.2]])
    # initialize cluster centers.
    c1 = (0.5, 0.5) #dataPoints[0]
    c2 = (0.4, 0.4) #dataPoints[7]
    m1 = c1
    m2 = c2

    cluster1 = np.zeros((8, 2))
    cluster2 = np.zeros((8, 2))
    count1 = 0 # number of points in cluster1
    count2 = 0 # number of points in cluster2
    count11 = 1
    count22 = 1

    while count1 != count11 and count2 != count22:

        count11 = count1
        count22 = count2
        count1 = 0
        count2 = 0
        m1 = c1
        m2 = c2
        p6cluster = ''
        for x in range (dataPoints.shape[0]):
            d1 = np.sqrt(((m1 - dataPoints[x]) * (m1 - dataPoints[x])).sum())
            d2 = np.sqrt(((m2 - dataPoints[x]) * (m2 - dataPoints[x])).sum())
            if(d1 < d2):
                cluster1[count1] = dataPoints[x]
                count1 = count1 + 1
                if x == 5:
                    p6cluster = 'cluster1'

            else:
                cluster2[count2] = dataPoints[x]
                count2 = count2 + 1
                if x == 5:
                    p6cluster = 'cluster2'
        # compute new centroids
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        for p in range(count1):
            x1 = x1 + cluster1[p][0]
            y1 = y1 + cluster1[p][1]

        for p in range(count2):
            x2 = x2 + cluster2[p][0]
            y2 = y2 + cluster2[p][1]

        c1 = (x1/count1, y1/count1)
        c2 = (x2/count2, y2/count2)

        plt.xlabel('X')
        plt.ylabel('Y')
        axis = plt.axis([0, 1, 0, 1])
        for cx in range(count1):
            plt.plot(cluster1[cx][0], cluster1[cx][1], 'k.', color='red')
        for cx in range(count2):
            plt.plot(cluster2[cx][0], cluster2[cx][1], 'k.', color='blue')

        # mark new centroids
        plt.plot(c1[0], c1[1], '*', color='black')
        plt.plot(c2[0], c2[1], '*', color='black')

        plt.show()
        plt.close()

    return p6cluster, count2, c1, c2








