__author__ = 'Soheil'
import collections
with open("TheMajorElement.txt", "r") as my_text:
    for line in my_text:
        seq = line.rstrip('\n').split(',')
        set = [item for item, count in collections.Counter(seq).items() if count > len(seq)/2]
        if len(set) != 0:
            print int(set[0])
        else:
            print 'None'
