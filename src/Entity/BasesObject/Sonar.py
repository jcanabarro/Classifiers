from src.Entity.Entity import Entity


class Sonar(Entity):

    def __init__(self):
        self.path = '../Bases/Sonar.csv'
        super(Sonar, self).__init__(self.path)

    def get_value(self, attr):
        return super(Sonar, self).get_value(attr)
