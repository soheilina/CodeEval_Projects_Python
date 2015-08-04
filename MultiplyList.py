__author__ = 'Soheil'

with open("MultiplyLists.txt", "r") as my_text:
    for line in my_text:
        a, b = line.rstrip('\n').split('|')
        num1 = a.split()
        num2 = b.split()
        result = [int(x)*int(y) for (x, y) in zip(num1, num2)]
        print ' '.join(map(str, result))
