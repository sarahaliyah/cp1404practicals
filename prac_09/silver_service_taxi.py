from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A Taxi with added flagfall and higher pricing based on fanciness"""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with name, fuel, and fanciness"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string representation including flagfall"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate fare including flagfall"""
        fare = super().get_fare()
        return round(self.flagfall + fare, 1)
