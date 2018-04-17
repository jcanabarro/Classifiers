from src.Entity.Entity import Entity


class Mammo(Entity):

    def __init__(self):
        self.path = '../Bases/Mammo.csv'
        super(Mammo, self).__init__(self.path)

    def get_value(self, attr):
        return super(Mammo, self).get_value(attr)

    def get_train_set(self):
        return super(Mammo, self).get_train_set()

    def get_test_set(self):
        return super(Mammo, self).get_test_set()

    def get_validation_set(self):
        return super(Mammo, self).get_validation_set()
