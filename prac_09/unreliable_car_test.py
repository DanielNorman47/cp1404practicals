"""
testing for unreliable car subclass
is all testing and a mess
"""
from unreliable_car import UnreliableCar

bad_car = UnreliableCar("Car but bad", 1000, 30)
fuel = bad_car.fuel
success_count = 0
for i in range(0, 100):
    bad_car.drive(10)
    print(bad_car.fuel != fuel)
    success_count += (1 if bad_car.fuel != fuel else 0)
    fuel = bad_car.fuel
print(success_count) # UnreliableCar works. Yipee.