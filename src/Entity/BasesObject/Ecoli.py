from src.Entity.Entity import Entity


class Ecoli(Entity):

    def __init__(self):
        self.path = '../Bases/Ecoli.csv'
        super(Ecoli, self).__init__(self.path)

    def get_value(self, attr):
        return super(Ecoli, self).get_value(attr)
