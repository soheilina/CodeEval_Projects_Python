__author__ = 'Soheil'

with open("StewiseWord.txt", "r") as my_text:
    for line in my_text:
        word = max(line.split(), key= len)
        for idx,letter in enumerate(word):
            print '*'*idx+letter,
        print
