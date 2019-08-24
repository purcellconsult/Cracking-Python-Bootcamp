#####################################
# Learn OOP by modeling cars
# --------------------------
# Learn OOP in python by modeling
# real world everyday objects.
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#####################################

from random import choice


class Car:
    """
    This class models a car in python.
    """
    def __init__(self, year, make, model):
        """
        Initializes the state of the car
        object.
        year: the year the car was manufactured.
        make: the brand of the vehicle.
        model: the name used by the manufacturer.
        """
        self.year = year
        self.make = make
        self.model = model
        self.speed = 0
        self.colors = ['white', 'silver', 'black', 'grey',
                       'blue', 'red', 'brown', 'green']

        self.car_color = choice(self.colors)

    def get_year(self):
        return self.year

    def get_make(self):
        return self.make

    def accelerate(self, amount=5):
        x = amount
        if self.speed < 300 and x < 60:
            self.speed += amount
        else:
            raise ValueError('Invalid Amount')

    def hit_brakes(self, amount=5):
        x = amount
        if self.speed > 0 and x < 60:
            self.speed -= amount
        else:
            raise ValueError('Invalid Amount')

    def is_stopped(self):
        if self.speed == 0:
            return True
        return False

    def is_moving(self):
        if self.speed > 0:
            return True
        else:
            return False

    def get_color(self):
        return self.car_color

    def speedometer(self):
        return '{} mph'.format(self.speed)


a = Car('2010', 'Honda', 'Civic Hatchback')
print(a.speedometer())
print(a.is_moving())
print(a.is_stopped())
a.accelerate()
a.accelerate()
print(a.speedometer())
print(a.year)
print(a.get_color())
a.hit_brakes(10)
print(a.speedometer())
