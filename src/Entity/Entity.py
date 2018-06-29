import os

import pandas as pd
import numpy as np

# Other functionality used by sklearn
from sklearn.model_selection import train_test_split
from src.Entity.BestParameters import BestParameters
from src.Entity.TestSet import TestSet
from src.Entity.TrainSet import TrainSet
from src.ToCsv import ToCsv


class Entity:

    def __init__(self, path):
        self.data_frame = pd.read_csv(path)
        self.path = os.path.split(path)[1]
        self.classifier = np.split(self.data_frame, [len(self.data_frame.columns) - 1], axis=1)
        self.samples = 0.5
        self.train_attributes, self.test_attributes, self.train_class, self.test_class = train_test_split(
            self.classifier[0], self.classifier[1], test_size=0.5, train_size=0.5)
        self.test_attributes, self.validate_attributes, self.test_class, self.validate_class = train_test_split(
            self.test_attributes, self.test_class, test_size=0.5, train_size=0.5)
        self.train_set = TrainSet(self.train_attributes, self.train_class, self.test_attributes, self.test_class,
                                  self.samples)
        self.best_param = BestParameters(self.validate_attributes, self.validate_class, self.test_attributes)
        self.test_set = TestSet(self.test_attributes, self.test_class)

    def get_value(self, attr):
        return self.data_frame[attr]

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

    # Function to train all the classifiers
    def get_trained_classifiers(self, neighbors):
        return self.train_set.get_trained_classifiers(neighbors)

    # Functions to combine the result of multiples classifiers
    def get_majority_rule(self, classifiers):
        return self.test_set.voting_classifier(classifiers, 'hard')

    def get_sum_rule(self, classifiers):
        return self.test_set.voting_classifier(classifiers, 'soft')

    # Function to test all the classifiers
    def get_tested_classifier(self, classifier, name):
        classifier_test_result = []
        classifier_proba_test_result = []
        for i in range(20):
            classifier_test_result.append(self.test_set.get_tested_classifier(classifier))
            classifier_proba_test_result.append(self.test_set.get_proba_tested_classifier(classifier))

        data_frame_result = pd.DataFrame(classifier_test_result).T
        data_frame_proba = pd.DataFrame.from_records(classifier_proba_test_result).T
        all_data_frames = [data_frame_result, data_frame_proba]
        for df in all_data_frames:
            df.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                          11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        # Path in this case already have the folder inside de function, and also have the csv extension
        ToCsv().save_on_csv(name + 'Result' + self.path, pd.concat(all_data_frames, axis=1).reset_index(drop=True))
