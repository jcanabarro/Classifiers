from src.Entity.Entity import Entity


class Haberman(Entity):

    def __init__(self):
        self.path = '../Bases/Haberman.csv'
        super(Haberman, self).__init__(self.path)

    def get_value(self, attr):
        return super(Haberman, self).get_value(attr)

    def get_train_set(self):
        return super(Haberman, self).get_train_set()

    def get_test_set(self):
        return super(Haberman, self).get_test_set()

    def get_validation_set(self):
        return super(Haberman, self).get_validation_set()
