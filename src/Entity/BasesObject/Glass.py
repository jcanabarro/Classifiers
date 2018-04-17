from src.Entity.Entity import Entity


class Glass(Entity):

    def __init__(self):
        self.path = '../Bases/Glass.csv'
        super(Glass, self).__init__(self.path)

    def get_value(self, attr):
        return super(Glass, self).get_value(attr)

    def get_train_set(self):
        return super(Glass, self).get_train_set()

    def get_test_set(self):
        return super(Glass, self).get_test_set()

    def get_validation_set(self):
        return super(Glass, self).get_validation_set()
