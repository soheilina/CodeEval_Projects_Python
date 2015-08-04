__author__ = 'Soheil'


def lowerCase(path):
    with open(path, "r") as my_file:
        print my_file.read().lower()

lowerCase("lowercase.txt")