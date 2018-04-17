from src.Entity.Entity import Entity


class Laryngeal3(Entity):

    def __init__(self):
        self.path = '../Bases/Laryngeal3.csv'
        super(Laryngeal3, self).__init__(self.path)

    def get_value(self, attr):
        return super(Laryngeal3, self).get_value(attr)
