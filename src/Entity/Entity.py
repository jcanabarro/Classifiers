import pandas as pd
import numpy as np

# Classifier imports
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.neural_network import MLPClassifier


class Entity:

    def __init__(self, path):
        self.data_frame = pd.read_csv(path)
        self.classifier = np.split(self.data_frame, [len(self.data_frame.columns) - 1], axis=1)
        self.train_attributes, self.test_attributes, self.train_class, self.test_class = train_test_split(
            self.classifier[0],
            self.classifier[1],
            test_size=0.5,
            train_size=0.5)
        self.test_attributes, self.validate_attributes, self.test_class, self.validate_class = train_test_split(
            self.test_attributes,
            self.test_class,
            test_size=0.5,
            train_size=0.5)

    def get_value(self, attr):
        return self.data_frame[attr]

    def generic_train(self, classifier):
        # In this case we need to do a ravel because fit don't expect a 1d matrix
        classifier.fit(self.train_attributes, np.ravel(self.train_class))
        return classifier.predict(self.test_attributes), self.test_class

    def get_svm(self):
        self.classifier = svm.SVC()
        return self.generic_train(self.classifier)

    def get_knn(self):
        self.classifier = KNeighborsClassifier(n_neighbors=3)
        return self.generic_train(self.classifier)

    def get_naive_bayes(self):
        self.classifier = GaussianNB()
        return self.generic_train(self.classifier)

    def get_tree_decision(self):
        self.classifier = tree.DecisionTreeClassifier()
        return self.generic_train(self.classifier)

    def get_mlp(self):
        self.classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
        return self.generic_train(self.classifier)
