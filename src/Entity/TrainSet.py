import numpy as np

# Classifier imports
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier


class TrainSet:

    def __init__(self, train_attributes, train_class, test_attributes, test_class):
        self.classifier = None
        self.train_attributes = train_attributes
        self.train_class = train_class
        self.test_attributes = test_attributes
        self.test_class = test_class

    def generic_train(self, classifier, samples):
        bagging = BaggingClassifier(classifier, max_samples=samples)
        # In this case we need to do a ravel because fit don't expect a 1d matrix
        np.seterr(divide='ignore', invalid='ignore')
        return bagging.fit(self.train_attributes, np.ravel(self.train_class))

    def get_trained_svm(self, samples):
        self.classifier = SVC(kernel='linear', probability=False, class_weight='balanced')
        return self.generic_train(self.classifier, samples)

    def get_trained_knn(self, neighbors, samples):
        self.classifier = KNeighborsClassifier(n_neighbors=neighbors)
        return self.generic_train(self.classifier, samples)

    def get_trained_naive_bayes(self, samples):
        self.classifier = GaussianNB()
        return self.generic_train(self.classifier, samples)

    def get_trained_tree_decision(self, samples):
        self.classifier = DecisionTreeClassifier()
        return self.generic_train(self.classifier, samples)

    def get_trained_mlp(self, samples):
        self.classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
        return self.generic_train(self.classifier, samples)
