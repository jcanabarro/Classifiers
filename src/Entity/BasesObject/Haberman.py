from src.Entity.Entity import Entity


class Haberman(Entity):

    def __init__(self):
        self.path = '../Bases/Haberman.csv'
        super(Haberman, self).__init__(self.path)

    def get_value(self, attr):
        return super(Haberman, self).get_value(attr)
