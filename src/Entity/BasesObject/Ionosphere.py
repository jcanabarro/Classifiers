from src.Entity.Entity import Entity


class Ionosphere(Entity):

    def __init__(self):
        self.path = '../Bases/Ionosphere.csv'
        super(Ionosphere, self).__init__(self.path)

    def get_value(self, attr):
        return super(Ionosphere, self).get_value(attr)
