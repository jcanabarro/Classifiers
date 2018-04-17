from src.Entity.Entity import Entity


class Phoneme(Entity):

    def __init__(self):
        self.path = '../Bases/Phoneme.csv'
        super(Phoneme, self).__init__(self.path)

    def get_value(self, attr):
        return super(Phoneme, self).get_value(attr)

    def get_train_set(self):
        return super(Phoneme, self).get_train_set()

    def get_test_set(self):
        return super(Phoneme, self).get_test_set()

    def get_validation_set(self):
        return super(Phoneme, self).get_validation_set()
