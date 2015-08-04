__author__ = 'Soheil'

with open("splitNumbers.txt", "r") as my_text:
    for line in my_text:
        a,b = line.rstrip("\n").split(" ")
        #print words
        if '-' in b:
            idx = b.index('-')
            print int(a[0:idx]) - int(a[idx:])
        elif '+' in b:
            idx = b.index('+')
            print int(a[0:idx]) + int(a[idx:])

