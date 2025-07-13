"""
Guitar test for DFS exercise
Guess time: 20m (up to playing the guitars)
Actual time: 12m (^^^)
"""
import guitar
gib = guitar.Guitar("Gibson L-5 CES", 1922, 16035.40)
other = guitar.Guitar("Guitar 2", 1976, 3.50)

print(f"gibson... get_age() Expected 103. Got {gib.get_age()}")
print(f"Guitar 2  get_age() Expected 49. Got {other.get_age()}")

print(f"gibson... is_vintage() - Expected true. Got {gib.is_vintage()}")
print(f"Guitar 2  is_vintage() - Expected false. Got {other.is_vintage()}")
