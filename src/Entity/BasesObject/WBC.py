from src.Entity.Entity import Entity


class Wbc(Entity):

    def __init__(self):
        self.path = '../Bases/WBC.csv'
        super(Wbc, self).__init__(self.path)

    def get_value(self, attr):
        return super(Wbc, self).get_value(attr)

    def get_train_set(self):
        return super(Wbc, self).get_train_set()

    def get_test_set(self):
        return super(Wbc, self).get_test_set()

    def get_validation_set(self):
        return super(Wbc, self).get_validation_set()
