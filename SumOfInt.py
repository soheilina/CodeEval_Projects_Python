__author__ = 'Soheil'

with open("SumOfInt.txt", "r") as my_text:
    print sum(int(x.rstrip("\n")) for x in my_text)
