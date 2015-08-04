__author__ = 'Soheil'

MorseCode= {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G',
	        '....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O',
	        '.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W',
	        '-..-':'X','-.--':'Y','--..':'Z','-----':'0','.----':'1','..---':'2','...--':'3',
	        '....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9'}
with open("MorseCode.txt", "r") as my_text:
    for line in my_text:
        words = line.rstrip('\n').split("  ")
        for word in words:
            letters = [MorseCode[c] for c in word.split()]
            print ''.join(letters),
        print


