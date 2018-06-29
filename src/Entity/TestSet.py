import numpy as np
from sklearn.ensemble import VotingClassifier


class TestSet:

    def __init__(self, test_attributes, test_class):
        self.test_attributes = test_attributes
        self.test_class = test_class

    def get_tested_classifier(self, classifier):
        return classifier.predict(self.test_attributes)

    def get_proba_tested_classifier(self, classifier):
        return classifier.predict_proba(self.test_attributes)

    def voting_classifier(self, classifiers, rule):
        result = VotingClassifier(estimators=[('knn', classifiers[0]), ('svm', classifiers[1]),
                                              ('dt', classifiers[2]), ('mlp', classifiers[3]),
                                              ('nb',classifiers[4])], voting=rule)
        result.fit(self.test_attributes, np.ravel(self.test_class))
        return result.predict(self.test_attributes)
