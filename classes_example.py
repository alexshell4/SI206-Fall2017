class Vehicle():
    def __init__(self, c):
        self.color = c

    def __str__(self):
        return 'Vehicle: color={}'.format(self.color)

class Bike(Vehicle):
    def __init__(self, type, c):
        Vehicle.__init__(self, c)
        self.type = type



vehicle_1 = Vehicle('blue')
vehicle_2 = Vehicle('red')
bike_1 = Bike('mountain', 'green')

print vehicle_1
print bike_1
