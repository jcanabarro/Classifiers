import os

import pandas as pd
import numpy as np

# Other functionality used by sklearn
from sklearn.model_selection import train_test_split
from src.Entity.BestParameters import BestParameters
from src.Entity.TestSet import TestSet
from src.Entity.TrainSet import TrainSet


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

    def get_proba(self, predictions):
        acc = 0
        for index, result in enumerate(predictions):
            expected = self.test_class.iloc[index][0]
            if expected == result:
                acc += 1
        return acc / len(self.test_class)

    # Functions to combine the result of multiples classifiers

    def fix_argmax_value(self, results):
        for idx, result in enumerate(results):
            results[idx] += 1
        return results

    def get_majority_rule(self, classifiers):
        return self.test_set.voting_classifier(classifiers, 'hard')

    def get_sum_rule(self, classifiers):
        sum_result = self.test_set.voting_classifier(classifiers, 'soft')
        return sum_result, self.get_proba(sum_result)

    def get_borda_rule(self, classifiers):
        borda_result = self.test_set.borda_count(classifiers)
        borda_result = self.fix_argmax_value(borda_result)
        return borda_result, self.get_proba(borda_result)

    def get_prod_rule(self, classifiers):
        prod_result = self.test_set.prod_rule(classifiers)
        prod_result = self.fix_argmax_value(prod_result)
        return prod_result, self.get_proba(prod_result)

    def get_max_rule(self, classifiers):
        max_result = self.test_set.max_rule(classifiers)
        max_result = self.fix_argmax_value(max_result)
        return max_result, self.get_proba(max_result)

    def get_min_rule(self, classifiers):
        min_result = self.test_set.min_rule(classifiers)
        min_result = self.fix_argmax_value(min_result)
        return min_result, self.get_proba(min_result)

    def get_mean_rule(self, classifiers):
        mean_result = self.test_set.mean_rule(classifiers)
        mean_result = self.fix_argmax_value(mean_result)
        return mean_result, self.get_proba(mean_result)

    def get_median_rule(self, classifiers):
        median_result = self.test_set.median_rule(classifiers)
        median_result = self.fix_argmax_value(median_result)
        return median_result, self.get_proba(median_result)
