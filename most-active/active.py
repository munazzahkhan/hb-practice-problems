"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""

    years_dict = {}
    for year in range(1900, 2000):
        years_dict[year] = 0

    for name, start, end in bio_data:
        value = []
        for year in range(start, end + 1):
            years_dict[year] += 1
  
    num_authors = years_dict.values()
    max_active = max(num_authors)
    max_active_period = []

    for key, value in years_dict.items():
        if value == max_active:
            max_active_period.append(key)
    
    start = max_active_period[0]
    i = 1
    for idx, year in enumerate(max_active_period):
        if idx != (len(max_active_period) - 1):
            if (max_active_period[i] - max_active_period[idx]) != 1:
                end = max_active_period[idx]
                break
        i += 1
    
    return (start, max_active_period[idx])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")