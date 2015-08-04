__author__ = 'Soheil'

with open("selfDescriptiveNumber.txt", "r") as my_text:
    for line in my_text:
        rep = 0
        for index,item in enumerate(line.rstrip("\n")):
            rep = line.count(str(index)) # rep = sum(1 if _ == str(index) else 0 for _ in line)
            if rep != int(item):
                print 0
                break
            rep = 0
        else:
            print 1