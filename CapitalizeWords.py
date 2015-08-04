__author__ = 'Soheil'

with open("CapitalizeWords.txt", "r") as my_text:
    for line in my_text:
        words = line.split()
        for word in words:
            print word[0].upper() + word[1:],
        print

        """ Alternative...
        sentence = [word[0].upper() + word[1:] for word in words]
        print " ".join(sentence)
        """

        """ Amin's Alternative...
        lst = [word[0].upper() + word[1:] if word[0].isalpha() else word for word in test.split() ]
		print ' '.join(lst)
		"""