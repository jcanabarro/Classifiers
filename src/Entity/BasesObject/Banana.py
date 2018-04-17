from src.Entity.Entity import Entity


class Banana(Entity):

    def __init__(self):
        self.path = '../Bases/Banana.csv'
        super(Banana, self).__init__(self.path)

    def get_value(self, attr):
        return super(Banana, self).get_value(attr)

    def get_train_set(self):
        return super(Banana, self).get_train_set()

    def get_test_set(self):
        return super(Banana, self).get_test_set()

    def get_validation_set(self):
        return super(Banana, self).get_validation_set()
