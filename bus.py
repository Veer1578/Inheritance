class vehicle():
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage


class bus(vehicle):
    pass

school_bus = bus('Volvo', 180, 12)
print(f'Vehicle name: {school_bus.name}, speed: {school_bus.speed}, mileage: {school_bus.mileage}')