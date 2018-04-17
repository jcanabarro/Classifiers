from src.Entity.Entity import Entity


class Ecoli(Entity):

    def __init__(self):
        self.path = '../Bases/Ecoli.csv'
        super(Ecoli, self).__init__(self.path)

    def get_value(self, attr):
        return super(Ecoli, self).get_value(attr)

    def get_train_set(self):
        return super(Ecoli, self).get_train_set()

    def get_test_set(self):
        return super(Ecoli, self).get_test_set()

    def get_validation_set(self):
        return super(Ecoli, self).get_validation_set()
