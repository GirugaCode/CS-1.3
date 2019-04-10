#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # Input is a word 'racecar'
    # Output should determine if it is a palindrome

    # Take the input text and turn it into a list of characters
    # Reverse the list
    # Compare that reversed list to the original list of charaters
    # Check by seeing if they contain the same index
    # Return true if so / if not Return false

    # Second Iteration, Covers all test cases
    # Removes the need for punctuations
    no_punctuation = str.maketrans('', '', string.punctuation)
    text = text.translate(no_punctuation)
    # Makes sure all texts are lowercase for the function
    text = text.lower()
    # Replaces all white spaces in text to none
    text = text.replace(' ', '')
    # Keeps track of the first and last index of the word
    first_index = 0
    last_index = len(text) - 1
    # As long as the first index is less than the last index
    while first_index < last_index:
        # Return False if the first and last indexes to not match
        if text[first_index] != text[last_index]:
            return False
        # Increment the first index and Decrease the last index to continue the while loop
        first_index += 1
        last_index -= 1
    return True

def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    print(is_palindrome('racecar'))
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
