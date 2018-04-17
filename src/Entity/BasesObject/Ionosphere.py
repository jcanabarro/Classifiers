from src.Entity.Entity import Entity


class Ionosphere(Entity):

    def __init__(self):
        self.path = '../Bases/Ionosphere.csv'
        super(Ionosphere, self).__init__(self.path)

    def get_value(self, attr):
        return super(Ionosphere, self).get_value(attr)

    def get_train_set(self):
        return super(Ionosphere, self).get_train_set()

    def get_test_set(self):
        return super(Ionosphere, self).get_test_set()

    def get_validation_set(self):
        return super(Ionosphere, self).get_validation_set()
