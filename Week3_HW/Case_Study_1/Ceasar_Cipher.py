# Let's look at the lowercase letters.
import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "

# create `letters` here!
letters = {index:letter for index, letter in enumerate(alphabet)}

print(letters)

alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

key = 3

l=len(alphabet)-key
# define `coded_message` here!

cm = dict(enumerate( alphabet[l:] +alphabet[:l]))

coded_message = {v:k for k, v in cm.items()}

print(letters)
print(coded_message)

message = "hi my name is caesar"


def caesar(message, key):
    # return the encoded message as a single string!
    alphabet = string.ascii_lowercase + " "
    letters = dict(enumerate(alphabet))
    l = len(alphabet) - key
    cm = dict(enumerate(alphabet[l:] + alphabet[:l]))
    coded_message = {v: k for k, v in cm.items()}

    # print(letters)
    # print(coded_message)
    r = ""
    for letter in message:
        r += letters[coded_message[letter]]
    return r


coded_message = caesar(message, 3)
print(coded_message)

import string


def caesar(message, key):
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted_alphabet)
    # print(table)
    return message.translate(table)


decoded_message = caesar(coded_message, -3)

print(decoded_message)