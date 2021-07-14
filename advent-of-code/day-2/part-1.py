"""
The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. 
"Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed 
by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) 
and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; 
it contains no instances of b, but needs at least 1. 
The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

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
        for char in password:
            if char == alphabet:
                count += 1
        if int(least) <= count <= int(most):
            valid_passwords += 1

    # print("occurance: ", occurance, "alphabet: ", alphabet, "password: ", password)
    # print("least: ", least, "most: ", most)
    # print("char: ", char)
    # print(data)
    # print((least, most), alphabet, password)

    return valid_passwords


print(num_valid_passwords())