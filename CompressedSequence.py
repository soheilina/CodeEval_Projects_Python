__author__ = 'Soheil'
import collections
with open("CompressedSequence.txt", "r") as my_text:
    for line in my_text:
        numbers = map(int, line.rstrip('\n').split())
        preserve_order = list(collections.OrderedDict.fromkeys(numbers))
        for i in preserve_order:
            print "%d %d" % (numbers.count(i), i),
        print