import numpy as np
from sklearn.model_selection import GridSearchCV


class BestParameters:

    def __init__(self, validate_attributes, validate_class, test_attributes):
        self.validate_attributes = validate_attributes
        self.validate_class = validate_class
        self.test_attributes = test_attributes
        self.classifier = None

    def get_best_params(self, classifier):
        print('oi')
        classifier.fit(self.validate_attributes, np.ravel(self.validate_class))
        print('oi')
        return classifier.best_params_, classifier

    def get_svm_best_param(self, classifier):
        tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-1, 1e-2, 1e-3, 1e-4],
                             'C': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]},
                            {'kernel': ['linear'], 'C': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]}]
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_knn_best_param(self, classifier):
        tuned_parameters = [{'algorithm': ['auto'], 'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]},
                            {'algorithm': ['ball_tree'], 'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]},
                            {'algorithm': ['kd_tree'], 'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]},
                            {'algorithm': ['brute'], 'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]}]
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_naive_bayes_best_param(self, classifier):
        tuned_parameters = {}
        classifier = GridSearchCV(classifier, tuned_parameters)
        print(classifier.get_params().keys())
        return self.get_best_params(classifier)

    def get_tree_decision_best_param(self, classifier):
        tuned_parameters = {
            "criterion": ["gini", "entropy"],
            "min_samples_split": [2, 10, 20],
            "max_depth": [None, 2, 5, 10],  # pruned
            "min_samples_leaf": [1, 5, 10],
            "max_leaf_nodes": [None, 5, 10, 20],  # pruned
        }
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_mlp_best_param(self, classifier):
        tuned_parameters = {
            'learning_rate': ["constant", "invscaling", "adaptive"],
            'hidden_layer_sizes': [(10, 2), (20, 2), (30, 2), (40, 2), (50, 2),
                                   (60, 2), (70, 2), (80, 2), (90, 2), (100, 2), ],
            'alpha': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
            'activation': ["logistic", "relu", "Tanh"],
            'max_iter': [100, 200, 300, 400, 500]
        }
        classifier = GridSearchCV(estimator=classifier, param_grid=tuned_parameters)
        return self.get_best_params(classifier)
