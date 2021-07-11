"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats:

>>> compress('aabbaabb')
'a2b2a2b2'

If a character appears once, it should not be followed by a number:

>>> compress('abc')
'abc'

The function should handle letters, whitespace, and punctuation:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""


def compress(string):
    """Return a compressed version of the given string."""

    result = string[0]
    i = 1
    j = 1
    while i<len(string):
        if string[i] == string[i-1]:
            if i == (len(string)-1):
                j += 1
                result += str(j)
            j += 1
        elif j == 1:
            result += string[i]
        else:
            result += str(j)
            result += string[i]
            j = 1
        i += 1
    
    return result



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
