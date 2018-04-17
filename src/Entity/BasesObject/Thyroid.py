from src.Entity.Entity import Entity


class Thyroid(Entity):

    def __init__(self):
        self.path = '../Bases/Thyroid.csv'
        super(Thyroid, self).__init__(self.path)

    def get_value(self, attr):
        return super(Thyroid, self).get_value(attr)
