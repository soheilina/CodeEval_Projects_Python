__author__ = 'Soheil'
Hex2Dec = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
with open("HexToDecimal.txt", "r") as my_text:
    for line in my_text:
        """ loooong alternative solution ->>>>
        temp =[c for c in line[::-1] if c != "\n"]
        print "temp: ", temp
        dec = 0
        for (index,char) in enumerate(temp):
            dec += Hex2Dec[char] * 16 ** index
        print dec
                """
        print int(line, 16)