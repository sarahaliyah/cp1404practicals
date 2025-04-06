from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """A Car that may fail to drive based on reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialise with name, fuel, and reliability"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive if random chance allows"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
