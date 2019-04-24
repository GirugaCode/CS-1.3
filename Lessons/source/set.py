#!python

from hashtable import HashTable
from linkedlist import LinkedList

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
        self.items.set(element, element)
        self.size += 1
    
    def remove(self, element):
        """Removes an element from the set."""
        self.items.delete(element)
        self.size -= 1
    
    def union(self, other_set):
        """ Returns a set that has that is a unity of two seperate sets"""
        union_set = Set()
        for element in self.items.keys():
            union_set.add(element)
        for element in other_set.items.keys():
            union_set.add(element)
        return union_set

    def intersection(self, other_set):
        """Returns a set that has common elements between two sets"""
        intersection_set = Set()
        
        for element in self.items.keys():
            if element in other_set.items.keys():
                intersection_set.add(element)
        return intersection_set

    def difference(self, other_set):
        """Returns the unique elements in the first set"""
        difference_set = Set()

        for element in self.items.keys():
            if element not in other_set.items.keys():
                difference_set.add(element)
        return difference_set

    def is_subset(self, other_set):
        """Checks if the set contains a part of the other set"""
        for element in self.items.keys():
            if element not in other_set.items.keys():
                return False
        return True


    