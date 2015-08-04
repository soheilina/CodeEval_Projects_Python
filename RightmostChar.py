__author__ = 'Soheil'

with open("RightmostChar.txt", "r") as my_text:
    for line in my_text:
        if line not in ['\n', '\r\n']:
            word, char = line.rstrip('\n').split(',')
            if char in word:
                print len(word) - word[::-1].index(char) - 1
            else:
                print -1

        """ Alternative...
        print word.rfind(char)
        """
