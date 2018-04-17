from src.Entity.Entity import Entity


class Wdvg(Entity):

    def __init__(self):
        self.path = '../Bases/WDVG.csv'
        super(Wdvg, self).__init__(self.path)

    def get_value(self, attr):
        return super(Wdvg, self).get_value(attr)
