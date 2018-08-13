import numpy as np
from brew.combination import Combiner
from sklearn.ensemble import VotingClassifier
from brew import Ensemble, EnsembleClassifier


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
                                              ('nb', classifiers[4])], voting=rule)
        result.fit(self.test_attributes, np.ravel(self.test_class))
        return result.predict(self.test_attributes)

    def generic_rule(self, classifiers, rule):
        self.test_attributes = self.test_attributes.reset_index(drop=True)
        ensemble = Ensemble(classifiers=[classifiers[0], classifiers[1], classifiers[2],
                                         classifiers[3], classifiers[4]])
        ensemble_clf = EnsembleClassifier(ensemble=ensemble, combiner=Combiner(rule))
        return ensemble_clf.predict(self.test_attributes)

    def borda_count(self, classifiers):
        self.predictions_ = list()
        for classifier in classifiers:
            self.predictions_.append(classifier.predict_proba(self.test_attributes))

        self.predictions_ = dict(np.ndenumerate(self.predictions_))
        scores = {}
        for l in self.predictions_:
            for idx, elem in enumerate(reversed(l)):
                if not elem in scores:
                    scores[elem] = 0
                else:
                    scores[elem] += idx
        return sorted(scores.keys(), key=lambda element: scores[element])

    def prod_rule(self, classifiers):
        self.predictions_ = list()
        for classifier in classifiers:
            self.predictions_.append(classifier.predict_proba(self.test_attributes))
        return np.prod(self.predictions_)
