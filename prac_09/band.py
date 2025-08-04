"""
band class
full of musicians
"""
class Band:
    """Band class"""
    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Musician."""
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of a band, showing the variables."""
        return str(vars(self))


    def add(self, musician):
        """Add a musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musicians in the band."""
        if not self.musicians:
            return f"{self.name} needs a musician!"
        return f"{self.name} contains: {self.musicians[0]}"