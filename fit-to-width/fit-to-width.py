"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

# import textwrap

def fit_to_width(string, limit):
    """Print string within a character limit."""

    # create a stack of words
    words = list(reversed(string.split()))
    lines = []
    curr_line = []

    while words:
        word = words[-1]

        # See if current word fits the line limit
        if len(" ".join(curr_line + [word])) <= limit:
            curr_line.append(words.pop())

        # if the word doesn't fir the limit, start a new line
        else:
            if curr_line:
                lines.append(" ".join(curr_line))
            curr_line = []
    
    # append the remaining line
    lines.append(" ".join(curr_line))

    # alternate one line solution
    # lines = textwrap.wrap(string, limit)

    for line in lines:
        print(line)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
