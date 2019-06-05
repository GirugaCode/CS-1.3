#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # Returns None if the item is not in the array
    if item not in array:
        return None
    # Find the item in the array until it has found the number
    elif array[index] == item:
        return index
    # Do a recursive search
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
    # Set the values of left and right as long as one of them are None
    if left == None or right == None:
        left = 0
        right = len(array) - 1

    # Same logic for the iterative approach
    middle_index = (right + left) // 2
    median_value = array[middle_index]

    if item == median_value:
        return middle_index

    if item > median_value:
        left = middle_index + 1

    if item < median_value:
        right = middle_index - 1

    # if the left and right values collide, set the item to where it collided. Return
    if right == left:
        if array[right] == item:
            return right
        return None

    return binary_search_recursive(array, item, left, right)
