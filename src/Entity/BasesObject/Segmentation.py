from src.Entity.Entity import Entity


class Segmentation(Entity):

    def __init__(self):
        self.path = '../Bases/Segmentation.csv'
        super(Segmentation, self).__init__(self.path)

    def get_value(self, attr):
        return super(Segmentation, self).get_value(attr)

    def get_train_set(self):
        return super(Segmentation, self).get_train_set()

    def get_test_set(self):
        return super(Segmentation, self).get_test_set()

    def get_validation_set(self):
        return super(Segmentation, self).get_validation_set()
