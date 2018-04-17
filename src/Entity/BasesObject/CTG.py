from src.Entity.Entity import Entity


class Ctg(Entity):

    def __init__(self):
        self.path = '../Bases/CTG.csv'
        super(Ctg, self).__init__(self.path)

    def get_value(self, attr):
        return super(Ctg, self).get_value(attr)

    def get_train_set(self):
        return super(Ctg, self).get_train_set()

    def get_test_set(self):
        return super(Ctg, self).get_test_set()

    def get_validation_set(self):
        return super(Ctg, self).get_validation_set()