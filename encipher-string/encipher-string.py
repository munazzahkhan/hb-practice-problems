"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""

    alphabets = {
                    0: "a",
                    1: "b", 
                    2: "c", 
                    3: "d", 
                    4: "e", 
                    5: "f", 
                    6: "g", 
                    7: "h", 
                    8: "i", 
                    9: "j", 
                    10: "k", 
                    11: "l", 
                    12: "m", 
                    13: "n", 
                    14: "o", 
                    15: "p", 
                    16: "q", 
                    17: "r", 
                    18: "s", 
                    19: "t", 
                    20: "u", 
                    21: "v", 
                    22: "w", 
                    23: "x", 
                    24: "y", 
                    25: "z"
                }

    encoded_txt = []

    for letter in txt:
        if letter.isalpha():
            for key, value in alphabets.items():
                if letter.lower() == value:
                    new_letter = alphabets[(key+shift)%26]
                    if letter == letter.upper():
                        new_letter = new_letter.upper()
                    encoded_txt.append(new_letter)
        else:
            encoded_txt.append(letter)

    return "".join(encoded_txt)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
