from src.Entity.Entity import Entity


class Vehicle(Entity):

    def __init__(self):
        self.path = '../Bases/Vehicle.csv'
        super(Vehicle, self).__init__(self.path)

    def get_value(self, attr):
        return super(Vehicle, self).get_value(attr)
