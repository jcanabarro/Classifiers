from src.Entity.Entity import Entity


class Liver(Entity):

    def __init__(self):
        self.path = '../Bases/Liver.csv'
        super(Liver, self).__init__(self.path)

    def get_value(self, attr):
        return super(Liver, self).get_value(attr)
