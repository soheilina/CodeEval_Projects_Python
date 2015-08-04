__author__ = 'Soheil'

with open("swapNumbers.txt", "r") as my_text:
    for line in my_text:
        swapped = [word[-1]+word[1:-1]+word[0] for word in line.rstrip('\n').split(" ")]
        print " ".join(swapped)