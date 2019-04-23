#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        if self.list.head == None:
            return True
        else: 
            return False

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return self.list.size

    def push(self, item):
        """
        Insert the given item on the top of this stack.
        Runtime: O(1)
        Condition: Adds the given item to the list
        """
        # Push given item
        self.list.prepend(item)


    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        if self.is_empty():
            return None
        return self.list.head.data

    def pop(self):
        """
        Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Runtime: O(1)
        Condition: Checks if the list is empty then removes the item in the from of the list
        """
        # Remove and return top item, if any
        if self.is_empty():
            raise ValueError('Stack is empty')
        data = self.list.head.data
        self.list.head = self.list.head.next
        self.list.size -= 1
        return data


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return len(self.list)

    def push(self, item):
        """
        Insert the given item on the top of this stack.
        Runtime: O(1)
        Condition: Adds the given item to the list
        """
        # Insert given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        if self.is_empty():
            return None
        else:
            return self.list[-1]

    def pop(self):
        """
        Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Runtime: O(1)
        Condition: Checks if the list is empty then removes the item in the from of the list
        """
        # Remove and return top item, if any
        if self.is_empty():
            raise ValueError("Stack is Empty")
        else:
            return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
