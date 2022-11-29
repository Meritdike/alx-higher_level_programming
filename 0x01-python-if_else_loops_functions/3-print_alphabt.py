#!/usr/bin/python3
for letter in range(97, 123):
    if letter is not 'q' and letter is not 'e':
        print("{:c}".format(letter), end="")
