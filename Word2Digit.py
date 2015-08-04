__author__ = 'Soheil'
Word2Digit = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }
with open("Word2Digit.txt", "r") as my_text:
    for line in my_text:
        words = [Word2Digit[x] for x in line.rstrip('\n').split(';')]
        print ''.join(words)


