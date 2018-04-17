from src.Entity.Entity import Entity


class Phoneme(Entity):

    def __init__(self):
        self.path = '../Bases/Phoneme.csv'
        super(Phoneme, self).__init__(self.path)

    def get_value(self, attr):
        return super(Phoneme, self).get_value(attr)
