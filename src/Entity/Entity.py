import os

import pandas as pd
import numpy as np

# Other functionality used by sklearn
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from src.Entity.BestParameters import BestParameters
from src.Entity.TestSet import TestSet
from src.Entity.TrainSet import TrainSet


def fix_argmax_value(results):
    for idx, result in enumerate(results):
        results[idx] += 1
    return results


def save_persistence_model(classifier, classifier_name, base_name):
    joblib.dump(classifier, '../ClassifierPersistenceModel/' + base_name + '/' + classifier_name + '.pkl')


def load_persistence_model(classifier, name):
    joblib.dump(classifier, '../ClassifierPersistenceModel/' + name + '.pkl')


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
        self.best_param = BestParameters(self.validate_attributes, self.validate_class)
        self.test_set = TestSet(self.test_attributes, self.test_class)
        self.score = []

    def get_value(self, attr):
        return self.data_frame[attr]

    # Functions to get all the better parameters
    def get_svm_best_param(self, classifier):
        classifier_result, score = self.best_param.get_svm_best_param(classifier)
        self.score.append(score)
        return classifier_result

    def get_knn_best_param(self, classifier):
        classifier_result, score = self.best_param.get_knn_best_param(classifier)
        self.score.append(score)
        return classifier_result

    def get_nb_best_param(self, classifier):
        classifier_result, score = self.best_param.get_nb_best_param(classifier)
        self.score.append(score)
        return classifier_result

    def get_dt_best_param(self, classifier):
        classifier_result, score = self.best_param.get_dt_best_param(classifier)
        self.score.append(score)
        return classifier_result

    def get_mlp_best_param(self, classifier):
        classifier_result, score = self.best_param.get_mlp_best_param(classifier)
        self.score.append(score)
        return classifier_result

    # Function to get the best params of a list of classifiers
    def set_best_params(self, classifiers):
        classifiers[0].base_estimator = self.get_knn_best_param(classifiers[0].base_estimator)
        classifiers[1].base_estimator = self.get_svm_best_param(classifiers[1].base_estimator)
        classifiers[2].base_estimator = self.get_dt_best_param(classifiers[2].base_estimator)
        classifiers[3].base_estimator = self.get_mlp_best_param(classifiers[3].base_estimator)
        classifiers[4].base_estimator = self.get_nb_best_param(classifiers[4].base_estimator)
        return classifiers

    # Function to train all the classifiers
    def get_trained_classifiers(self, neighbors):
        return self.train_set.get_trained_classifiers(neighbors)

    # Function to get proba result
    def get_proba(self, predictions):
        acc = 0
        for index, result in enumerate(predictions):
            expected = self.test_class.iloc[index][0]
            if expected == result:
                acc += 1
        return acc / len(self.test_class)

    # Function to combine the result of multiples classifiers
    def get_rule(self, classifiers, rule_name, base_name):
        rule_result = []
        if rule_name == 'sum':
            rule_result = self.test_set.sum_rule(classifiers)
        elif rule_name == 'prod':
            rule_result = self.test_set.prod_rule(classifiers)
        elif rule_name == 'max':
            rule_result = self.test_set.max_rule(classifiers)
        elif rule_name == 'min':
            rule_result = self.test_set.min_rule(classifiers)
        elif rule_name == 'median':
            rule_result = self.test_set.median_rule(classifiers)
        elif rule_name == 'mean':
            rule_result = self.test_set.mean_rule(classifiers)
        elif rule_name == 'ranking':
            rule_result = self.test_set.ranking_rule(classifiers)
        elif rule_name == 'borda':
            rule_result = self.test_set.borda_rule(classifiers)
        elif rule_name == 'majority':
            rule_result = self.test_set.majority_rule(classifiers)
        elif rule_name == 'single' and base_name != 'blood':
            rule_result = self.test_set.single_best_rule(classifiers, np.argmax(self.score))
        elif rule_name == 'oracle':
            return self.get_proba(self.test_set.oracle_rule(classifiers))
        return self.get_proba(fix_argmax_value(rule_result))
