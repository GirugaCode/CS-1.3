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

    # Decode digits from binary (base 2)
    if base == 2: 
        # Keep track of the sum of the numbers
        sum = 0
        # A variable for the power
        power = len(digits) - 1

        # Iterate through the list of digits
        for num in digits:
            # Create a reference to the index this will create the input digits
            binary_index = string.digits.index(num)
            # Increment the sum by the index of the loop times the base to the power
            sum += binary_index * (base ** power)
            # Decrement the power
            power -= 1
        # Return the sum
        print("Base 2:", sum)

    # Decode digits from hexadecimal (base 16)
    if base == 16:
        sum = 0
        power = len(digits) - 1

        for num in digits:
            hex_index = string.hexdigits.index(num)        
            sum += hex_index * (base ** power)
            power -= 1
        print("Base 16:", sum)

    # Decode digits from any base (2 up to 36)
    sum = 0
    power = len(digits) - 1

    for num in digits:
        num_index = string.printable.index(num)
        sum += num_index * (base ** power)
        power -= 1
    print("Base 2 to 36:", sum)
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
    # Encode number in binary (base 2)
    if base == 2:
        result = ''
        while number != 0:
            # Divides the number with the base and ignores the remainder
            quotient = number // base
            print('Quotient:', quotient)
            # Manually set the remainder seperatly 
            remainder = number % base
            print('Remainder:', remainder)
            # Putting the remainder in the string for results
            result += str(remainder)
            print('Encoded Number:', result)
            # Determines to keep looping
            number = quotient
            print('Number:', number)
        # Reverse the lists
        return (result[::-1])

    # Encode number in hexadecimal (base 16)
    if base == 16:
        result = ''
        while number != 0:
            quotient = number // base
            remainder = number % base
            if remainder:
                remainder = string.hexdigits[remainder]
                result += str(remainder)
                number = quotient
            else:
                result += str(remainder)
                number = quotient
        return (result[::-1])
    # Encode number in any base (2 up to 36)
    result = ''

    while number != 0:
        remainder = number % base
        quotient = number // base
        if remainder:
            # Sets the remainder to the index of the list
            remainder = string.printable[remainder]
            # Add to string
            result += str(remainder)
            # Determines to keep looping
            number = quotient
        else:
            result += str(remainder)
            number = quotient
    # Reverse the string
    return (result[::-1])


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # Convert digits from any base to any base (2 up to 36)
    decoded_digits = decode(digits, base1)
    encoded_digits = encode(decoded_digits, base2)
    return encoded_digits

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
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
    print(encode(255, 16))
