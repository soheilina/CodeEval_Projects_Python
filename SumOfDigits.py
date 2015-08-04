__author__ = 'Soheil'
with open("SomeOfDigits.txt", "r") as my_text:
    for line in my_text:
        print sum(int(x) for x in line.rstrip("\n"))
