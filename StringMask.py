__author__ = 'Soheil'

with open("StringMask.txt", "r") as my_text:
    for line in my_text:
        string, bits = line.rstrip('\n').split()
        mask = lambda c,d: c.upper() if d == '1' else c
        maskedString = [mask(c,d) for (c,d) in zip(string,bits)]
        print "".join(maskedString)
