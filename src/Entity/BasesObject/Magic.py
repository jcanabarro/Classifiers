from src.Entity.Entity import Entity


class Magic(Entity):

    def __init__(self):
        self.path = '../Bases/Magic.csv'
        super(Magic, self).__init__(self.path)

    def get_value(self, attr):
        return super(Magic, self).get_value(attr)
