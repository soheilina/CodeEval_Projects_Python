__author__ = 'Soheil'

with open("penultimateWord.txt", "r") as my_text:

    for line in my_text:
        print [x for x in line.split()][-2]

        """
        temp = line.rstrip()[::-1]
        #print temp
        word = ""
        check = False

        for c in temp:
            if c != " ":
                if check == True:
                    #print "c: ", c
                    word += c
                    if temp.index(c) == len(temp)-1:
                        print word[::-1]
                else:
                    continue
            elif check == True:
                #print "len(temp): ", len(temp)
                #print "temp.index(c)", temp.index(c)
                print word[::-1]
                check = False
                break
            elif c == " ":
                 check = True
                 """
