__author__ = 'Soheil'

with open("FindWriter.txt", "r") as my_text:
    for line in my_text:
        writer = ""
        if line not in ['\n', '\r\n']:
            code, key = line.rstrip('\n').split('| ')
            for i in key.split():
                writer += code[int(i)-1]
            print writer
