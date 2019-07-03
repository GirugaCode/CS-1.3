#!python

from hashtable import HashTable

class Set():
    
    def __init__(self, elements=None):
        """Initialized this Set with the given data."""
        self.items = HashTable()
        self.size = 0
        if elements is not None:
            for item in elements:
                self.add(item)
    
    def length(self):
        """Calculates the length of the set."""
        return self.items.length()
    
    def contains(self, element):
        """Checks if the element is in the set."""
        return self.items.contains(element)

    def add(self, element):
        """Adds an element to the set."""
        self.items.set(element, element) # Think of the data as a tuple, they both point to the same place in memeory
        self.size += 1
    
    def remove(self, element):
        """Removes an element from the set."""
        self.items.delete(element)
        self.size -= 1
