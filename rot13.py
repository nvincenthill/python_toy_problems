# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using "encode" in Python is considered cheating.

import string
from codecs import encode as _dont_use_this_


def rot13(message):
    ciphered = ''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(0, len(message)):
        is_uppercase = message[i] in alphabet
        rot_index = alphabet.index(message[i].lower()) + 13
        new_index = rot_index if rot_index < 26 else rot_index - 26
        ciphered += alphabet[new_index] if is_uppercase else alphabet[new_index].upper()
    return ciphered

# tests

# print(rot13("test") == "grfg")
# print(rot13("Test") == "Grfg")
