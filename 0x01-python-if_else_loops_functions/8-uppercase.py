#!/usr/bin/python3
def to_upper(character):
    if ord(charachter) >= and ord(charachter) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)

    def uppercase(str):
        new = ""
        for character in str:
            new += "%c" % to_upper(charachter)
        print("{:s}".format(new))
