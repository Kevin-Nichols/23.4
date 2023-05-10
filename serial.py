"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Makes a new generator at the number provided (otherwise it starts at 0) and assigns said number to 'new' for incrementing the number, and 'start' for remembering the starting number."""
        self.start = self.new = start
        
    
    def generate(self):
        """Adds one to 'new' and returns 'new' minus one to show the correct beginning serial number and subsequent serial numbers."""
        self.new += 1
        return self.new -1
    
    def reset(self):
        """Resets the 'new' serial number to the 'start' number."""
        self.new = self.start
        
    def __repr__(self):
        """Display representation"""
        return f"<SerialGenerator start={self.start} new={self.new}>"
