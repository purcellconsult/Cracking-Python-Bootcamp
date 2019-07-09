#######################################
# OOP concepts in python:
# -----------------------
#
# Topics: inheritance, polymorphism,
# abstraction, and encapsulation.
#
# Data of dog breeds taken from:
# https://www.akc.org
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
########################################

from random import choice
import fractions


class Dog:
    def __init__(self):
        self.height = None
        self.weight = None
        self.life_expectancy = []
        self.temperament = []
        self.group = None
        self.akc_popularity = fractions.Fraction()


class AiredaleTerrier(Dog):
    """
    Inheritance: AiredaleTerrier inherits
    from the Dog class.
    """
    def __init__(self):
        self.height = '{} inches'.format(23)
        self.weight = [weight for weight in range(50, 70)]
        self.life_expectancy = [life for life in range(11, 14)]
        self.temperament = ['friendly', 'clever', 'courageous']
        self.group = 'Terrier Group'
        self.akc_popularity = fractions.Fraction(60, 193)


class BichonFrise(Dog):
    """
    Inheritance: BichonFrise inherits
    from the Dog class.
    """
    def __init__(self):
        self.height = [height for height in range(9.5, 11.5)]
        self.weight = [weight for weight in range(12, 18)]
        self.life_expectancy = [life for life in range(14, 15)]
        self.temperament = ['playful', 'curious', 'peppy']
        self.group = 'Non-Sporting Group'
        self.akc_popularity = fractions.Fraction(46, 193)


class Chihuahua(Dog):
    """
    Inheritance: Chihuahua inherits
    from the Dog class.
    """
    def __init__(self):
        self.height = [height for height in range(14, 16)]
        self.weight = [weight for weight in range(1, 6)]
        self.life_expectancy = [life for life in range(14, 16)]
        self.temperament = ['charming', 'graceful', 'sassy']
        self.group = 'Toy Group'
        self.akc_popularity = fractions.Fraction(33, 193)


class Rottweiler(Dog):
    """
    Inheritance: Rottweiler inherits
    from the Dog class.
    """
    def __init__(self):
        self.height = [24, 25, 26, 27]
        self.weight = [weight for weight in range(95, 135)]
        self.life_expectancy = [9, 10]
        self.group = 'Working Group'
        self.akc_popularity = fractions.Fraction(8, 193)


class MyDog(Rottweiler):
    """
    Inheritance: MyDog inherits
    from Rottweiler class. It also
    adds additional functionality
    not found in the Dog class
    """

    def __init__(self):
        super().__init__()  # calls the superclass constructor

    def my_dog_hobbies(self):
        return ['frisbee', 'hikes', 'eating']

    def favorite_treat(self):
        return 'apples'

    def favorite_dog_park(self):
        return 'Fort Woof'


jack = MyDog() # instance of MyDog
print(choice(jack.height))
print(choice(jack.weight), 'lbs')
print(choice(jack.life_expectancy))
print(jack.group)
print(jack.akc_popularity)
print(jack.my_dog_hobbies())
print(jack.favorite_treat())
print(jack.favorite_dog_park())

# polymorphism, greek for 'many forms'
# There's many types of dogs

bella = AiredaleTerrier()
molly = BichonFrise()
charlie = Chihuahua()
rocky = Rottweiler()

