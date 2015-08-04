__author__ = 'Soheil'
import collections
with open("LowestUniqueNumber.txt", "r") as my_text:
    for line in my_text:
        players = line.rstrip('\n').split()
        set = [item for item,count in collections.Counter(players).items() if count == 1]
        if len(set) != 0:
            print players.index(min(set))+1
        else:
            print 0

