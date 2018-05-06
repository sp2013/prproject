from sklearn import datasets
from sklearn import svm



class ML:
    """"""
    def __init__(self,):
        """Constructor for ML"""

    def train(self):
        iris = datasets.load_iris()
        clf = svm.SVC(gamma=0.001, C=100.)
        X, y = iris.data, iris.target
        clf.fit(X, y)
        