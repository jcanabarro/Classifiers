import numpy as np

# Classifier imports
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier


def get_svm():
    return SVC(kernel='linear', probability=False, class_weight='balanced')


def get_knn(neighbors):
    return KNeighborsClassifier(n_neighbors=neighbors)


def get_nb():
    return GaussianNB()


def get_dt():
    return DecisionTreeClassifier()


def get_mlp():
    return MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)


class TrainSet:

    def __init__(self, train_attributes, train_class, test_attributes, test_class, samples):
        self.classifier = []
        self.train_attributes = train_attributes
        self.train_class = train_class
        self.test_attributes = test_attributes
        self.test_class = test_class
        self.samples = samples
        self.bagging = []

    def generic_train(self, classifiers):
        for base_estimator in classifiers:
            self.bagging.append(BaggingClassifier(base_estimator=base_estimator, max_samples=self.samples). \
                                fit(self.train_attributes, np.ravel(self.train_class)))
        # In this case we need to do a ravel because fit don't expect a 1d matrix
        return self.bagging

    def get_trained_classifiers(self, neighbors):
        return self.generic_train([get_knn(neighbors), get_svm(), get_dt(), get_mlp(), get_nb()])
        # return self.generic_train([get_mlp()])
