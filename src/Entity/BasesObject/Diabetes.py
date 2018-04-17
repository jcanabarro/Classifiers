from src.Entity.Entity import Entity


class Diabetes(Entity):

    def __init__(self):
        self.path = '../Bases/Diabetes.csv'
        super(Diabetes, self).__init__(self.path)

    def get_value(self, attr):
        return super(Diabetes, self).get_value(attr)

    def get_train_set(self):
        return super(Diabetes, self).get_train_set()

    def get_test_set(self):
        return super(Diabetes, self).get_test_set()

    def get_validation_set(self):
        return super(Diabetes, self).get_validation_set()
