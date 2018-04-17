from src.Entity.Entity import Entity


class Magic(Entity):

    def __init__(self):
        self.path = '../Bases/Magic.csv'
        super(Magic, self).__init__(self.path)

    def get_value(self, attr):
        return super(Magic, self).get_value(attr)

    def get_train_set(self):
        return super(Magic, self).get_train_set()

    def get_test_set(self):
        return super(Magic, self).get_test_set()

    def get_validation_set(self):
        return super(Magic, self).get_validation_set()
