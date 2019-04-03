#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
    
def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # key_list = string.printable
    # exponent = len(digits) - 1

    # for digit in digits:
    #     print("digit: ",digit)
    #     print("digits: ",digits)
    #     print("base: ",base)
    #     print("exponent: ",exponent)
    #     print("key_list: ",key_list)

    # TODO: Decode digits from binary (base 2)
    if base == 2: 
        digits_to_list = (list(map(int, digits)))
        sum = 0
        power = len(digits_to_list) - 1

        for index in digits_to_list:
            sum += index * (base ** power)
            power -= 1
        print(sum)
    
    # TODO: Decode digits from hexadecimal (base 16)
    if base == 16:
        list_of_hex = string.hexdigits
        digits_to_list_two = (list (digits))
        power = len(digits_to_list_two) - 1
        sum = 0

        for char in digits_to_list_two:
            hex_index = list_of_hex.index(char)
            sum += hex_index * (base ** power)
            power -= 1
        print(sum)

    # TODO: Decode digits from any base (2 up to 36)
    list_of_printable = string.printable
    list_of_chars = (list(digits))
    power = len(list_of_chars) - 1
    sum = 0 


    for char in list_of_chars:
        char_index = list_of_printable.index(char)
        sum += char_index * (base ** power)
        power -= 1


    return sum



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)

    if base == 2:
        encoded_number = ''
        while number != 0:
            # Divides the number with the base and ignores the remainder
            quotient = number // base
            # Manually set the remainder seperatly 
            remainder = number % base
            # Putting the remainder in the string for results
            encoded_number += str(remainder)
            number = quotient
        return (encoded_number[::-1])

    # TODO: Encode number in hexadecimal (base 16)

    # TODO: Encode number in any base (2 up to 36)

    list_of_printable = string.printable
    encoded_number = ''

    while number != 0:
        remainder = number % base
        print("remainder: ", remainder)
        quotient = number // base
        print("quotient: ", quotient)
        if remainder > 9:
            # Sets the remainder to the index of the list
            remainder = list_of_printable[remainder]
            # Add to string
            encoded_number += str(remainder)
            # Determines to keep looping
            number = quotient
        else:
            encoded_number += str(remainder)
            number = quotient
    # Reverse the string
    return (encoded_number[::-1])


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    print("Decode Test: ", decode('yeet', 36))
    print("Encode Test: ", encode(48, 16))
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
