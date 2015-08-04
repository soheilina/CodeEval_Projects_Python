__author__ = 'Soheil'

with open("EvenNumbers.txt", "r") as testCases:
    for test in testCases:
        if int(test) % 2 == 0:
            print 1
        else:
            print 0
