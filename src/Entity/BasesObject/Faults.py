from src.Entity.Entity import Entity


class Faults(Entity):

    def __init__(self):
        self.path = '../Bases/Faults.csv'
        super(Faults, self).__init__(self.path)

    def get_value(self, attr):
        return super(Faults, self).get_value(attr)

    def get_train_set(self):
        return super(Faults, self).get_train_set()

    def get_test_set(self):
        return super(Faults, self).get_test_set()

    def get_validation_set(self):
        return super(Faults, self).get_validation_set()
