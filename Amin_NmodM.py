#!/usr/bin/python

#!/Users/Soheil/PycharmProjects/CodeEval/Easy/NmodM.txt

__author__ = 'Soheil'


import sys
with open(sys.argv[0]) as test_cases:
    for test in test_cases:
        a,b = [int(x) for x in test.split(',')]
        while a >= b:
            a -= b
        print a
