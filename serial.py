class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""
    
    def __init__(self, start=0):
        """Initialize the SerialGenerator with a starting value."""
        self.start = self.current = start
        
    def __repr__(self):
        """Shows the current and starting values."""
        return f"<SerialGenerator start={self.start} current={self.current}>"

    def generate(self):
        """Generate the next serial number."""
        result = self.current
        self.current += 1
        return result
    
    def reset(self):
        """Reset the serial generator to the starting value."""
        self.current = self.start
        return self.start
