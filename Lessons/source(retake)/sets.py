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
        """Calculates the length of the set.
        Runtime: O(n) where n is the number of times we iterate through the buckets
        to check the length
        """
        return self.items.length()
    
    def contains(self, element):
        """Checks if the element is in the set.
        Runtime: O(1) constant time because we are just checking the value and 
        using the hash function to check the bucket index
        """
        return self.items.contains(element)

    def add(self, element):
        """Adds an element to the set.
        Runtime: O(1) constant time on average to hash the value and place it in a corresponding bucket
        """
        self.items.set(element, element) # Think of the data as a tuple, they both point to the same place in memeory
        self.size += 1
    
    def remove(self, element):
        """Removes an element from the set.
        Runtime: O(1) constant time to find the bucket and delete the item
        """
        self.items.delete(element)
        self.size -= 1