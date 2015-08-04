__author__ = 'Soheil'

with open("DataRecovery.txt", "r") as my_text:
    for line in my_text:
        set, seq = line.rstrip('\n').split(';')
        words = set.split()
        numbers = map(int, seq.split())

        for i in range(1,len(words)+1):
            if i not in numbers:
                numbers.append(i)
                break

        for n,w in sorted( zip(numbers, words)):
            print w,
        print

