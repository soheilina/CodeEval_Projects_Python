__author__ = 'Soheil'
hiddenDigits={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
with open("HiddenDigits.txt", "r") as my_text:
    for line in my_text:
        """
        check = False
        digits = ""
        for char in line:
            if ord(char) in range(97, 107):
                digits +=  str (ord(char) - 97)
                check = True
            elif ord(char) in range(49, 58):
                digits +=  str (ord(char) - 48)
                check = True

        if check == False:
            print "NONE"
        else:
            print digits """
        temp1 = [n for n in line if (n <= 'j' and n >= 'a') or n.isdigit()]
        res = [str(ord(n) - ord('a')) if n <= 'j' and n >= 'a' else n for n in temp1]
        if len(res):
            print ''.join(res)
        else:
            print "NONE"