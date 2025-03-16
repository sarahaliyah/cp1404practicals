"""
Estimated time: 20 minutes
Time taken: 25 minutes
"""


class Guitar:
    """Represents a guitar with a name, year of manufacture, and cost."""
    def __init__(self, name, year, cost):
        """Initialize a Guitar instance with its name, year of manufacture, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the guitar's age based on the current year."""
        return 2022 - self.year

    def is_vintage(self):
        """Determine if the guitar is considered vintage (50 years or older)."""
        return self.get_age() >= 50
