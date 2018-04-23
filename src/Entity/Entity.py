import pandas as pd
import numpy as np

# Other functionality used by sklearn
from sklearn.model_selection import train_test_split

from src.Entity.BestParameters import BestParameters
from src.Entity.TrainSet import TrainSet


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
        self.train_set = TrainSet(self.train_attributes, self.train_class, self.test_attributes, self.test_class)
        self.best_param = BestParameters(self.validate_attributes, self.validate_class, self.test_attributes)

    def get_value(self, attr):
        return self.data_frame[attr]

    # Function to train all the classifiers
    def get_svm(self):
        return self.train_set.get_trained_svm()

    def get_knn(self, neighbors):
        return self.train_set.get_trained_knn(neighbors)

    def get_naive_bayes(self):
        return self.train_set.get_trained_naive_bayes()

    def get_tree_decision(self):
        return self.train_set.get_trained_tree_decision()

    def get_mlp(self):
        return self.train_set.get_trained_mlp()

    # Functions to get all the better parameters
    def get_svm_best_param(self, classifier):
        return self.best_param.get_svm_best_param(classifier)

    def get_knn_best_param(self, classifier):
        return self.best_param.get_knn_best_param(classifier)

    def get_naive_bayes_best_param(self, classifier):
        return self.best_param.get_naive_bayes_best_param(classifier)

    def get_tree_decision_best_params(self, classifier):
        return self.best_param.get_tree_decision_best_param(classifier)

    def get_mlp_best_param(self, classifier):
        return self.best_param.get_mlp_best_param(classifier)
