__author__ = 'Soheil'

with open("readMore.txt", "r") as my_text:
    print "the number of lines: ", sum(1 for _ in my_text) # '_' is just a variable name! Py Stile!!!
with open("readMore.txt", "r") as my_text:
    for line in my_text:
        if len(line) > 55:
            s = line[0:40]
            for index , char in enumerate(s[::-1]):
                if char == " ":
                    idx = 40 - (index +1)
                    print line[0:idx] + "... <Read More>"
                    break
                elif index == 39:
                    print s + "... <Read More>"
        else:
            print line[0:len(line)-1]