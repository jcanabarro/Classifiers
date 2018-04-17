from src.Entity.Entity import Entity


class Liver(Entity):

    def __init__(self):
        self.path = '../Bases/Liver.csv'
        super(Liver, self).__init__(self.path)

    def get_value(self, attr):
        return super(Liver, self).get_value(attr)

    def get_train_set(self):
        return super(Liver, self).get_train_set()

    def get_test_set(self):
        return super(Liver, self).get_test_set()

    def get_validation_set(self):
        return super(Liver, self).get_validation_set()
