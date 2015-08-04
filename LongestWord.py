__author__ = 'Soheil'

with open("LongestWord.txt", "r") as my_text:
    for line in my_text:
        # temp = line.rstrip("\n").split(" ")
        # print temp
        print max(line.rstrip("\n").split(" "), key=lambda x: len(x))