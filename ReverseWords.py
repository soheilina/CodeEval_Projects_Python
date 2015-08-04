__author__ = 'Soheil'

with open("ReversWords.txt", "r") as my_text:
    for line in my_text:
        if line in ['\n', '\r\n']:
            print
        else:
            reversed = [word for word in line.rstrip('\n').split()[::-1]]
            print ' '.join(reversed)
