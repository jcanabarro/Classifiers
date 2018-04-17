from src.Entity.Entity import Entity


class Faults(Entity):

    def __init__(self):
        self.path = '../Bases/Faults.csv'
        super(Faults, self).__init__(self.path)

    def get_value(self, attr):
        return super(Faults, self).get_value(attr)
