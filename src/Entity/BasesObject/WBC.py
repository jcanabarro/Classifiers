from src.Entity.Entity import Entity


class Wbc(Entity):

    def __init__(self):
        self.path = '../Bases/WBC.csv'
        super(Wbc, self).__init__(self.path)

    def get_value(self, attr):
        return super(Wbc, self).get_value(attr)
