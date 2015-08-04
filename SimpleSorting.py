__author__ = 'Soheil'

with open("SimpleSorting.txt", "r") as my_text:
    for line in my_text:
        nums = sorted([float(num) for num in line.rstrip('\n').split()])
        print " ".join(["%.3f" % x for x in nums])
