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
        return classifier.best_params_, classifier.predict(self.test_attributes)

    def get_svm_best_param(self, classifier):
        tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-1, 1e-2, 1e-3, 1e-4],
                             'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]},
                            {'kernel': ['linear'], 'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}]
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_knn_best_param(self, classifier):
        tuned_parameters = [{'algorithm': ['auto'], 'n_neighbors': [5, 10, 15, 20, 25]},
                            {'algorithm': ['ball_tree'], 'n_neighbors': [5, 10, 15, 20, 25]},
                            {'algorithm': ['kd_tree'], 'n_neighbors': [5, 10, 15, 20, 25]},
                            {'algorithm': ['brute'], 'n_neighbors': [5, 10, 15, 20, 25]}, ]
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_naive_bayes_best_param(self, classifier):
        tuned_parameters = {
            'vec__max_df': (0.5, 0.625, 0.75, 0.875, 1.0),
            'vec__max_features': (None, 5000, 10000, 20000),
            'vec__min_df': (1, 5, 10, 20, 50),
            'tfidf__use_idf': (True, False),
            'tfidf__sublinear_tf': (True, False),
            'vec__binary': (True, False),
            'tfidf__norm': ('l1', 'l2'),
            'clf__alpha': (1, 0.1, 0.01, 0.001, 0.0001, 0.00001)
        }
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_tree_decision_best_param(self, classifier):
        tuned_parameters = {
            "criterion": ["gini", "entropy"],
            "min_samples_split": [2, 10, 20],
            "max_depth": [None, 2, 5, 10],
            "min_samples_leaf": [1, 5, 10],
            "max_leaf_nodes": [None, 5, 10, 20],
        }
        classifier = GridSearchCV(classifier, tuned_parameters)
        return self.get_best_params(classifier)

    def get_mlp_best_param(self, classifier):
        tuned_parameters = {
            'learning_rate': ["constant", "invscaling", "adaptive"],
            'hidden_layer_sizes': [(100, 1), (100, 2), (100, 3)],
            'alpha': [10.0 ** -np.arange(1, 7)],
            'activation': ["logistic", "relu", "Tanh"]
        }
        classifier = GridSearchCV(estimator=classifier, param_grid=tuned_parameters, n_jobs=-1, verbose=2, cv=10)
        return self.get_best_params(classifier)
