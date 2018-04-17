from src.Entity.Entity import Entity


class Diabetes(Entity):

    def __init__(self):
        self.path = '../Bases/Diabetes.csv'
        super(Diabetes, self).__init__(self.path)

    def get_value(self, attr):
        return super(Diabetes, self).get_value(attr)
