from car import Car
from random import randint

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        self.reliability = reliability
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def drive(self, distance):
        """drive distance if random numbers is less than reliability."""
        if randint(0, 100) < self.reliability:
            super().drive(distance)