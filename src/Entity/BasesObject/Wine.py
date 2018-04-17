from src.Entity.Entity import Entity


class Wine(Entity):

    def __init__(self):
        self.path = '../Bases/Wine.csv'
        super(Wine, self).__init__(self.path)

    def get_value(self, attr):
        return super(Wine, self).get_value(attr)

    def get_train_set(self):
        return super(Wine, self).get_train_set()

    def get_test_set(self):
        return super(Wine, self).get_test_set()

    def get_validation_set(self):
        return super(Wine, self).get_validation_set()
