import numpy as np
from sklearn.model_selection import GridSearchCV


class BestParameters:

    def __init__(self, validate_attributes, validate_class, test_attributes):
        self.validate_attributes = validate_attributes
        self.validate_class = validate_class
        self.test_attributes = test_attributes
        self.classifier = None

    def get_best_params(self, classifier):
        classifier.fit(self.validate_attributes, np.ravel(self.validate_class))
        return classifier.best_params_, classifier

    def get_svm_best_param(self, classifier):
        tuned_parameters = [{'base_estimator__kernel': ['rbf'], 'base_estimator__gamma': [1e-1, 1e-2, 1e-3, 1e-4],
                             'base_estimator__C': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
                             'base_estimator__class_weight':[{0: w} for w in [1, 2, 4, 6, 10]]},
                            {'base_estimator__kernel': ['linear'],
                             'base_estimator__C': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
                             'base_estimator__class_weight':[{0: w} for w in [1, 2, 4, 6, 10]]}]
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_knn_best_param(self, classifier):
        tuned_parameters = [{'base_estimator__algorithm': ['auto'],
                             'base_estimator__n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]},
                            {'base_estimator__algorithm': ['ball_tree'],
                             'base_estimator__n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]},
                            {'base_estimator__algorithm': ['kd_tree'],
                             'base_estimator__n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]},
                            {'base_estimator__algorithm': ['brute'],
                             'base_estimator__n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]}]
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_naive_bayes_best_param(self, classifier):
        tuned_parameters = {}
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_tree_decision_best_param(self, classifier):
        tuned_parameters = {
            "base_estimator__criterion": ["gini", "entropy"],
            "base_estimator__min_samples_split": [2, 10, 20],
            "base_estimator__splitter": ["best", "random"],
            "base_estimator__max_depth": [None, 5, 10, 20],  # pruned
            "base_estimator__min_samples_leaf": [1, 5, 10],
            "base_estimator__max_leaf_nodes": [None, 5, 10, 20],  # pruned
        }
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_mlp_best_param(self, classifier):
        tuned_parameters = {
            'base_estimator__learning_rate': ["constant", "invscaling", "adaptive"],
            'base_estimator__hidden_layer_sizes': [(10,), (20,), (30,), (40,), (50,),
                                   (60,), (70,), (80,), (90,), (100,)],
            'base_estimator__alpha': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            'base_estimator__activation': ["logistic", "relu"],
            'base_estimator__max_iter': [100, 200, 300, 400, 500]
        }
        classifier = GridSearchCV(estimator=classifier, param_grid=tuned_parameters)
        return self.get_best_params(classifier)
