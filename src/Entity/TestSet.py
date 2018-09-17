import numpy as np
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


class TestSet:

    def __init__(self, test_attributes, test_class):
        self.predictions_ = list()
        self.test_attributes = test_attributes
        self.test_class = test_class

    def predictions_result(self, classifiers):
        predictions_ = list()
        for classifier in classifiers:
            predictions_.append(classifier.predict_proba(self.test_attributes))
        return predictions_

    def voting_classifier(self, classifiers, rule):
        result = VotingClassifier(estimators=[('knn', classifiers[0]), ('svm', classifiers[1]),
                                              ('dt', classifiers[2]), ('mlp', classifiers[3]),
                                              ('nb', classifiers[4])], voting=rule)
        result.fit(self.test_attributes, np.ravel(self.test_class))
        return result.predict(self.test_attributes)

    def borda_count(self, classifiers):
        for classifier in classifiers:
            predictions = []
            for prediction in classifier.predict_proba(self.test_attributes):
                sorted_by_class = sorted([(prob, index + 1) for index, prob in enumerate(prediction)])
                sorted_by_index = sorted([(index, weight + 1) for weight, (prob, index) in enumerate(sorted_by_class)])
                predictions.append([weight for prob, weight in sorted_by_index])
            self.predictions_.append(predictions)
        return np.argmax(np.sum(np.array(self.predictions_), axis=0), axis=-1)

    def prod_rule(self, classifiers):
        return np.argmax(np.prod(self.predictions_result(classifiers), axis=0), axis=-1)

    def max_rule(self, classifiers):
        return np.argmax(np.max(self.predictions_result(classifiers), axis=0), axis=-1)

    def min_rule(self, classifiers):
        return np.argmax(np.min(self.predictions_result(classifiers), axis=0), axis=-1)

    def median_rule(self, classifiers):
        return np.argmax(np.median(self.predictions_result(classifiers), axis=0), axis=-1)

    def mean_rule(self, classifiers):
        return np.argmax(np.mean(self.predictions_result(classifiers), axis=0), axis=-1)

    def test_classifier(self, classifier):
        classifier = classifier.predict(self.test_attributes)
        return accuracy_score(self.test_class, classifier)
