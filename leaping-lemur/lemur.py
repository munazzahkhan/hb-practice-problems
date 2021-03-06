"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    i = 0 
    jumps = 0

    while i < (len(branches)-1):
        if (i+2) >= len(branches) or branches[i+2] == 1:
            i += 1
        else:
            i += 2
        jumps += 1
    
    return jumps



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE JUMPING!\n")