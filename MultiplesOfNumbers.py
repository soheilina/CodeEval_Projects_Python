__author__ = 'Soheil'

with open("MultiplesOfNumbers.txt", "r") as my_text:
    for line in my_text:
        a, b = line.rstrip('\n').split(',')
        x, n = int(a), int(b)
        if n >= x:
            print n
        else:
            while n < x:
                n *= 2
            print n