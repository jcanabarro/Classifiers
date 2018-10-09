import numpy as np
from sklearn.model_selection import GridSearchCV


class BestParameters:

    def __init__(self, validate_attributes, validate_class):
        self.validate_attributes = validate_attributes
        self.validate_class = validate_class
        self.classifier = None

    def get_best_params(self, classifier_model):
        classifier_model.fit(self.validate_attributes, np.ravel(self.validate_class))
        return classifier_model.best_estimator_, classifier_model.best_score_

    def get_svm_best_param(self, classifier):
        tuned_parameters = [{'kernel': ['rbf','linear', 'poly'], 'gamma': [1e-1, 1e-2, 1e-3, 1e-4],
                             'C': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
                             }]
        svm_model = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(svm_model)

    def get_knn_best_param(self, classifier):
        tuned_parameters = [{'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
                             'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]}]
        knn_model = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(knn_model)

    def get_nb_best_param(self, classifier):
        tuned_parameters = {}
        nb_model = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(nb_model)

    def get_dt_best_param(self, classifier):
        tuned_parameters = {
            "criterion": ["gini", "entropy"],
            "min_samples_split": [2, 10, 20],
            "splitter": ["best", "random"],
            "max_depth": [None, 5, 10, 20],  # pruned
            "min_samples_leaf": [1, 5, 10],
            "max_leaf_nodes": [None, 5, 10, 20],  # pruned
        }
        dt_model = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(dt_model)

    def get_mlp_best_param(self, classifier):
        tuned_parameters = {
            'learning_rate': ["constant", "invscaling", "adaptive"],
            'hidden_layer_sizes': [(20,), (20, 20,), (20, 20, 20),
                                   (40,), (40, 40,), (40, 40, 40),
                                   (60,), (60, 60,), (60, 60, 60),
                                   (80,), (80, 80,), (80, 80, 80),
                                   (100,), (100, 100,), (100, 100, 100)],
            'max_iter': [100, 200, 300, 400, 500]
        }
        mlp_model = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(mlp_model)
