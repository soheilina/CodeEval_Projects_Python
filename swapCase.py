__author__ = 'Soheil'

with open("swapCase.txt", "r") as my_text:
    text = ""
    for line in my_text:
        for char in line:
            ascii = ord(char)
            if ascii in xrange(97,123): # if char.islower():
                text += chr(ascii - 32)
            elif ascii in xrange(65, 91): # if char.isupper()
                text += chr(ascii + 32)
            else:
                text += char
    print text