#!/usr/bin/python3
for letter in range(97, 123):
    if letter is not 101 and letter is not 113:
        print("{:c}".format(letter), end="")
