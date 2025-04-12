CURRENT_YEAR = 2022

class Guitar:
    """Represents a guitar with a name, year of manufacture, and cost."""
    def __init__(self, name, year, cost):
        """Initialize a Guitar instance with its name, year of manufacture, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the guitar's age based on the current year."""
        return CURRENT_YEAR - self.year

    def __lt__(self, other):
        """Define less than operator for the sorting by year"""
        return self.year < other.year
