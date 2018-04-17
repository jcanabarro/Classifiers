from src.Entity.Entity import Entity


class Blood(Entity):

    def __init__(self):
        self.path = '../Bases/Blood.csv'
        super(Blood, self).__init__(self.path)

    def get_value(self, attr):
        return super(Blood, self).get_value(attr)
