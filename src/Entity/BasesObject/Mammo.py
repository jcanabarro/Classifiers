from src.Entity.Entity import Entity


class Mammo(Entity):

    def __init__(self):
        self.path = '../Bases/Mammo.csv'
        super(Mammo, self).__init__(self.path)

    def get_value(self, attr):
        return super(Mammo, self).get_value(attr)
