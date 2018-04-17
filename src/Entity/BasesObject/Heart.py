from src.Entity.Entity import Entity


class Heart(Entity):

    def __init__(self):
        self.path = '../Bases/Heart.csv'
        super(Heart, self).__init__(self.path)

    def get_value(self, attr):
        return super(Heart, self).get_value(attr)
