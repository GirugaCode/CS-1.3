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
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # Input is a word 'racecar'
    # Output should determine if it is a palindrome

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
    # Checks if the text is just one character
    if len(text) <= 1:
        return True
    # Checks if text is two of the same charaters
    if left is not None and left >= right:
        return True
    # Keeps track of the first and last index of the word
    if left == None or right == None:
        text = text.lower()
        left = 0
        right = len(text) - 1
    # Increase the left value if it runs into a space or punctuations
    while text[left] in string.punctuation + ' ':
        left += 1
    # Decrease the right value if it runs into a space or punctuations
    while text[right] in string.punctuation + ' ':
        right -= 1
    # Return False if the first and last indexes to not match
    if text[left] != text[right]:
        return False
    # Increment the first index and Decrease the last index to continue the while loop
    left += 1
    right -= 1
    # Recursive Call
    return is_palindrome_recursive(text, left, right)



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    print(is_palindrome('noon'))
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
