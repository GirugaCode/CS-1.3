#!python

def contains(text, pattern):
    """
    Return a boolean indicating whether pattern occurs in text.
    Runtime: O(n)
    Condition: Traverses through text to find the pattern
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern in text:
        return True
    else:
        return False

def find_index(text, pattern):
    """
    Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Runtime: O(n)
    Condition: Iterates over the text to find the pattern
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Iterates through and appends the index if the pattern finds the match for all indexes
    for index, _ in enumerate(text):
        try:
            if pattern == text[index: (index + len(pattern))]:
                return index # pattern == slice
        except:
            return 0
    return None

def find_all_indexes(text, pattern):
    """
    Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Runtime: O(n)
    Condition: Iterates over the text to find the pattern
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Empty list to store the indexes of the pattern
    pattern_indexes = []

    # Appends to the the pattern_indexes if the pattern is empty
    if pattern == '':
        for index in range(0, len(text)):
            pattern_indexes.append(index)
        return pattern_indexes

    # Iterates through and appends the index if the pattern finds the match for all indexes
    for index, _ in enumerate(text):
        if pattern == text[index: (index + len(pattern))]:
                pattern_indexes.append(index)
    return pattern_indexes

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    find_all_indexes('abc', 'bc')
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
