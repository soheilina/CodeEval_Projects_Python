__author__ = 'Soheil'
import re
with open("CleanUpTheWords.txt", "r") as my_text:
    for line in my_text:
         wordChars = re.findall("[a-zA-Z]+", line) # findes any alphabetic chars and its trailing
         print " ".join(wordChars).lower()