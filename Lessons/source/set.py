#!python

from hashtable import HashTable
from linkedlist import LinkedList

class Set():
    
    def __init__(self, elements=None):
        """Initialized this Set with the given data."""
        self.ht = HashTable()
        self.size = 0
        if elements is not None:
            for item in elements:
                self.ht.set(item, item)
    
    def length(self):
        """Calculates the length of the set."""
        return self.ht.length()
    
    def contains(self, element):
        """Checks if the element is in the set."""
        return self.ht.contains(element)

    def add(self, element):
        """Adds an element to the set."""
        self.ht.set(element, element)
    
    def remove(self, element):
        """Removes an element from the set."""
        self.ht.delete(element)
    