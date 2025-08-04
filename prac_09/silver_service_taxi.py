"""SilverServiceTaxi class def"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.5
    def __init__(self, name, fuel, fanciness):
        """Initialise an SST instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = super().price_per_km * self.fanciness

    def get_fare(self):
        """add the flag fall to the fare price."""
        return super().get_fare() + (self.flagfall if (super().get_fare()>0) else 0)

    def __str__(self):
        """add the flag fall to the description"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
