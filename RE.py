__author__ = 'Soheil'
import re
with open("RE.txt", "r") as my_text:
    for line in my_text:
        emails = re.findall("[\w\.]+\@[\.\w+]*\.com", line)
        print emails
