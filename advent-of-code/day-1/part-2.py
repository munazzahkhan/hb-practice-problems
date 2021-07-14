""" 

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. 
They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. 
Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""

def find_nums(num):

    file = open("expense-report.txt")
    entries = []

    for f in file:
        entries.append(int(f))
    
    set_entries = set(entries)

    for num1 in entries:
        for num2 in entries:
            num3 = num - (num1 + num2)
            if num3 in set_entries:
                prod = num1 * num2 * num3
            

    return prod

print(find_nums(2020))