from src.Entity.Entity import Entity


class Adult(Entity):

    def __init__(self):
        self.path = '../Bases/Adult.csv'
        super(Adult, self).__init__(self.path)

    def get_value(self, attr):
        return super(Adult, self).get_value(attr)

    def get_train_set(self):
        return super(Adult, self).get_train_set()

    def get_test_set(self):
        return super(Adult, self).get_test_set()

    def get_validation_set(self):
        return super(Adult, self).get_validation_set()
