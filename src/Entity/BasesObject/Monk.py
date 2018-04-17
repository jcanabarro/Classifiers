from src.Entity.Entity import Entity


class Monk(Entity):

    def __init__(self):
        self.path = '../Bases/Monk.csv'
        super(Monk, self).__init__(self.path)

    def get_value(self, attr):
        return super(Monk, self).get_value(attr)
