from src.Entity.Entity import Entity


class Ilpd(Entity):

    def __init__(self):
        self.path = '../Bases/ILPD.csv'
        super(Ilpd, self).__init__(self.path)

    def get_value(self, attr):
        return super(Ilpd, self).get_value(attr)

    def get_train_set(self):
        return super(Ilpd, self).get_train_set()

    def get_test_set(self):
        return super(Ilpd, self).get_test_set()

    def get_validation_set(self):
        return super(Ilpd, self).get_validation_set()
