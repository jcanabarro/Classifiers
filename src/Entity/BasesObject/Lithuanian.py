from src.Entity.Entity import Entity


class Lithuanian(Entity):

    def __init__(self):
        self.path = '../Bases/Lithuanian.csv'
        super(Lithuanian, self).__init__(self.path)

    def get_value(self, attr):
        return super(Lithuanian, self).get_value(attr)
