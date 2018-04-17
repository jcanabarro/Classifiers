from src.Entity.Entity import Entity


class German(Entity):

    def __init__(self):
        self.path = '../Bases/German.csv'
        super(German, self).__init__(self.path)

    def get_value(self, attr):
        return super(German, self).get_value(attr)
