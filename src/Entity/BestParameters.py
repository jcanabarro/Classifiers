import numpy as np
from sklearn.model_selection import GridSearchCV

from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import tree
from sklearn.neural_network import MLPClassifier


class BestParameters:

    def __init__(self, train_attributes, train_class):
        self.train_attributes = train_attributes
        self.train_class = train_class
        self.classifier = None

    def get_best_params(self, classifier):
        classifier.fit(self.train_attributes, np.ravel(self.train_class))
        return classifier.best_params_

    def get_svm_best_param(self):
        tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-1, 1e-2, 1e-3, 1e-4],
                             'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]},
                            {'kernel': ['linear'], 'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}]
        self.classifier = GridSearchCV(svm.SVC(), tuned_parameters)
        return self.get_best_params(self.classifier)

    def get_knn_best_param(self):
        tuned_parameters = [{'algorithm': ['auto'], 'n_neighbors': [5, 10, 15, 20, 25]},
                            {'algorithm': ['ball_tree'], 'n_neighbors': [5, 10, 15, 20, 25]},
                            {'algorithm': ['kd_tree'], 'n_neighbors': [5, 10, 15, 20, 25]},
                            {'algorithm': ['brute'], 'n_neighbors': [5, 10, 15, 20, 25]},]
        self.classifier = GridSearchCV(KNeighborsClassifier(), tuned_parameters)
        return self.get_best_params(self.classifier)

    def get_naive_bayes_best_params(self):
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
        self.classifier = GridSearchCV(MultinomialNB(), tuned_parameters)
        return self.get_best_params(self.classifier)

    def get_tree_decision_best_params(self):
        pass

    def get_mlp_best_params(self):
        pass
