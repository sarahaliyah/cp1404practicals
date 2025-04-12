class Band:
    """A class to represent a music band consisting of multiple musicians"""
    def __init__(self, name=""):
        """Create a new Band instance with a given name and an empty list of musicians"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string showing the band's name and a list of its musicians"""
        return f"{self.name} ({','.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band"""
        self.musicians.append(musician)

    def play(self):
        """Simulate the band playing by returning what each musician is playing"""
        return "\n".join(musician.play() for musician in self.musicians)
