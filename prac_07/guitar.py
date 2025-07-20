"""class definition for guitar"""

class Guitar:
    """guitar object class"""
    def __init__(self, name="", year=0, cost=0):
        """initialisation"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """string representation"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """return age since creation"""
        return 2025 - self.year

    def is_vintage(self):
        """if greater or equal to 50y old"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """if self is less than other"""
        return self.get_age() < other.get_age()