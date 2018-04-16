from src.Entity.Entity import Entity


class Banana(Entity):

    def __init__(self):
        self.path = '../Bases/Banana.csv'
        super(Banana, self).__init__(self.path)

    def get_values(self, attr):
        return super(Banana, self).get_value(attr)
