from src.Entity.Entity import Entity


class Weaning(Entity):

    def __init__(self):
        self.path = '../Bases/Weaning.csv'
        super(Weaning, self).__init__(self.path)

    def get_value(self, attr):
        return super(Weaning, self).get_value(attr)
