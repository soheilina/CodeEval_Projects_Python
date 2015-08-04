__author__ = 'Soheil'

with open("LettercasePercentageRation.txt", "r") as my_text:
    for line in my_text:
        up, lo = 0, 0
        up = sum(1 for letter in line.strip('\n') if letter.isupper())
        upPercentage = 100 * float(up)/len(line.rstrip('\n'))
        print "lowercase: %.2f uppercase: %.2f" % (100 - upPercentage, upPercentage)

