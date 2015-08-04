__author__ = 'Soheil'

with open("shortestRepetition.txt", "r") as my_text:
    string = ""
    for line in my_text:
        for char in line:
            if char not in string:
                string += char
            else:
