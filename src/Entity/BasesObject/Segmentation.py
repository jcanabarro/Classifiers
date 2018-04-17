from src.Entity.Entity import Entity


class Segmentation(Entity):

    def __init__(self):
        self.path = '../Bases/Segmentation.csv'
        super(Segmentation, self).__init__(self.path)

    def get_value(self, attr):
        return super(Segmentation, self).get_value(attr)
