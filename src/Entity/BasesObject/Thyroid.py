from src.Entity.Entity import Entity


class Thyroid(Entity):

    def __init__(self):
        self.path = '../Bases/Thyroid.csv'
        super(Thyroid, self).__init__(self.path)

    def get_value(self, attr):
        return super(Thyroid, self).get_value(attr)

    def get_train_set(self):
        return super(Thyroid, self).get_train_set()

    def get_test_set(self):
        return super(Thyroid, self).get_test_set()

    def get_validation_set(self):
        return super(Thyroid, self).get_validation_set()
