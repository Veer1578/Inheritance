class vehicle:
    def __init__(self, type):
        self.type = type
        print('Vehicle type is', type)

class car(vehicle):
    def __init__(self):
        vehicle.__init__('Car')

print(issubclass(car, vehicle))