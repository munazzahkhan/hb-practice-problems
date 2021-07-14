"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 10, 1, 9, 8], 10)
    6
    
    """

    i = 0
    if len(nums) != max_num:
        while i < len(nums):
            for idx, num in enumerate(sorted(nums)):
                if (idx + 1) != num:
                    return idx + 1
            if nums[-1] != max_num:
                return max_num
            i += 1
    else:
        return None

    """ Another simple mathematical solution """

    # expected = sum(range(max_num + 1))

    # return expected - sum(nums)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
