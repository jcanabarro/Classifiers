from src.Entity.Entity import Entity


class Heart(Entity):

    def __init__(self):
        self.path = '../Bases/Heart.csv'
        super(Heart, self).__init__(self.path)

    def get_value(self, attr):
        return super(Heart, self).get_value(attr)

    def get_train_set(self):
        return super(Heart, self).get_train_set()

    def get_test_set(self):
        return super(Heart, self).get_test_set()

    def get_validation_set(self):
        return super(Heart, self).get_validation_set()
