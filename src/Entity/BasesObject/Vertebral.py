from src.Entity.Entity import Entity


class Vertebral(Entity):

    def __init__(self):
        self.path = '../Bases/Vertebral.csv'
        super(Vertebral, self).__init__(self.path)

    def get_value(self, attr):
        return super(Vertebral, self).get_value(attr)

    def get_train_set(self):
        return super(Vertebral, self).get_train_set()

    def get_test_set(self):
        return super(Vertebral, self).get_test_set()

    def get_validation_set(self):
        return super(Vertebral, self).get_validation_set()
