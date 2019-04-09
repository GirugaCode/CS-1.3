#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # Return None if the item was never in the array
    if not array:
        return None 
    # Trying to find item in the array until the it returns the correct number
    elif array[index] == item: 
        return index
    # Using recursive
    else:
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # Setting up the first and last index of array
    first_index = 0
    last_index = len(array) - 1
    

    while first_index <= last_index:
        # Find the middle point of the list index
        middle_index = (first_index + last_index) // 2
        # Set the middle_index into a variable to change
        middle_value = array[middle_index]

        # if item is already in the middle, return it
        if item == middle_value:
            return middle_index
        # if the item is more than the middle index then focus on the middle to right of th array
        if item > middle_value:
            first_index = middle_index + 1
        # if the item is less than the middle index then focus on the middle to left of the array
        if item < middle_value:
            last_index = middle_index - 1

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    names = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']
    yeet = binary_search(names, 'Alex')
    print(yeet)

if __name__ == '__main__':
    main()