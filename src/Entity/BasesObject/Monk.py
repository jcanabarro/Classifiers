from src.Entity.Entity import Entity


class Monk(Entity):

    def __init__(self):
        self.path = '../Bases/Monk.csv'
        super(Monk, self).__init__(self.path)

    def get_value(self, attr):
        return super(Monk, self).get_value(attr)

    def get_train_set(self):
        return super(Monk, self).get_train_set()

    def get_test_set(self):
        return super(Monk, self).get_test_set()

    def get_validation_set(self):
        return super(Monk, self).get_validation_set()
