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
    
    def union(self, other_set):
        """ Returns a set that has that is a unity of two seperate sets
        Runtime: O(n) where n is the amount of items we have to search through to add to the set
        """
        union_set = Set()
        for key, value in self.items:
            union_set.add(key)
        for key, value in other_set.items:
            union_set.add(key)
        return union_set

    def intersection(self, other_set):
        """Returns a set that has common elements between two sets
        Runtime: O(n) where n is the amount of items we have to search through to add to the set
        """
        intersection_set = Set()
        
        for key, value in self.items:
            if other_set.contains(key):
                intersection_set.add(key)
        return intersection_set

    def difference(self, other_set):
        """Returns the unique elements in the first set
        Runtime: O(n) where n is the amount of items we have to search through to add to the set
        """
        difference_set = Set()

        for key, value in self.items:
            if not other_set.contains(key):
                difference_set.add(key)
        return difference_set

    def is_subset(self, other_set):
        """Checks if the set contains a part of the other set
        Runtime: O(n) where n is the amount of items we have to search through to check the items
        """
        for key, value in self.items:
            if not other_set.contains(key):
                return False
        return True
