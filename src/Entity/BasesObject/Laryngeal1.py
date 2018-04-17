from src.Entity.Entity import Entity


class Laryngeal1(Entity):

    def __init__(self):
        self.path = '../Bases/Laryngeal1.csv'
        super(Laryngeal1, self).__init__(self.path)

    def get_value(self, attr):
        return super(Laryngeal1, self).get_value(attr)

    def get_train_set(self):
        return super(Laryngeal1, self).get_train_set()

    def get_test_set(self):
        return super(Laryngeal1, self).get_test_set()

    def get_validation_set(self):
        return super(Laryngeal1, self).get_validation_set()
