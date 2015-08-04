__author__ = 'Soheil'
import re
with open("MixedContent.txt", "r") as my_text:
    for line in my_text:
        words = re.findall('[a-zA-Z]+', line)
        numbers = re.findall('[\d]+', line)
        if len(words) != 0 and len(numbers) != 0:
            print ','.join(words) + '|' + ','.join(numbers)
        elif len(words) != 0:
            print ','.join(words)
        elif len(numbers) != 0:
            print ','.join(numbers)
        else:
            print

