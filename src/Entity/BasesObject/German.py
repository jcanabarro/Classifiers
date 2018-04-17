from src.Entity.Entity import Entity


class German(Entity):

    def __init__(self):
        self.path = '../Bases/German.csv'
        super(German, self).__init__(self.path)

    def get_value(self, attr):
        return super(German, self).get_value(attr)

    def get_train_set(self):
        return super(German, self).get_train_set()

    def get_test_set(self):
        return super(German, self).get_test_set()

    def get_validation_set(self):
        return super(German, self).get_validation_set()
