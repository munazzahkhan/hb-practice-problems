"""
The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job 
at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, 
and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain 
the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

"""


def num_valid_passwords():

    file = open("passwords.txt")
    data = []

    for line in file:
        occurance, char, password = line.rstrip().split(" ")
        least, most = occurance.split("-")
        alphabet = char[0]
        data.append([(least, most), alphabet, password])

    valid_passwords = 0

    for entry in data:
        (least, most), alphabet, password = entry
        count = 0
        if password[int(least)-1] == alphabet:
            count += 1
        if password[int(most)-1] == alphabet:
            count += 1
        if count == 1:
            valid_passwords += 1

    return valid_passwords


print(num_valid_passwords())