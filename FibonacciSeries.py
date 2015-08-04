__author__ = 'Soheil'

with open("FibonacciSeries.txt", "r") as my_text:
    for line in my_text:
        n = int(line.rstrip('\n'))
        a, b = 0, 1
        fibo = lambda b: a, b = b , a+b if True: range(n)
        print
        fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]