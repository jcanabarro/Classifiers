class TestSet:

    def __init__(self, test_attributes, test_class):
        self.test_attributes = test_attributes
        self.test_class = test_class

    def get_tested_classifier(self, classifier):
        return classifier.predict(self.test_attributes)

    def get_proba_tested_classifier(self, classifier):
        return classifier.predict_proba(self.test_attributes)
