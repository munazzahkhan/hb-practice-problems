""" The Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. 
Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

"""

def find_nums(num):

    file = open("expense-report.txt")
    entries = []

    for f in file:
        entries.append(int(f))
    
    set_entries = set(entries)

    for entry in entries:
        diff = num - entry
        if diff in set_entries:
            num2 = entry * diff
          

    return num2

print(find_nums(2020))