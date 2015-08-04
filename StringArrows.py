__author__ = 'Soheil'
import re
with open("StringArrows.txt", "r") as my_text:
    for line in my_text:
        #print line
        line = line.replace('->>-', '->>>>-')
        line = line.replace('-<<-', '-<<<<-')
        #print line
        arrows = re.findall("[\>][\>][\-][\-][\>]|[\<][\-][\-][\<][\<]", line)
        #print arrows
        print len(arrows)
