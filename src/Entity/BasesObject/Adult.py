from src.Entity.Entity import Entity


class Adult(Entity):

    def __init__(self):
        self.path = '../Bases/Adult.csv'
        super(Adult, self).__init__(self.path)

    def get_value(self, attr):
        return super(Adult, self).get_value(attr)
