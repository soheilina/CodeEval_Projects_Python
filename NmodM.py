__author__ = 'Soheil'


with open("NmodM.txt", "r") as my_file:
    for case in my_file:
        N, M = [int(x) for x in case.split(',')]
        result = N % M
        print "for N=%d and M=%d mod(N,M) = %d" %(N, M, result)
