from src.Entity.Entity import Entity


class Ilpd(Entity):

    def __init__(self):
        self.path = '../Bases/ILPD.csv'
        super(Ilpd, self).__init__(self.path)

    def get_value(self, attr):
        return super(Ilpd, self).get_value(attr)
