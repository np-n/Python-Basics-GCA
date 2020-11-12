
"""
    A module demonstrating vowel and consonants count 
"""

import string

vowel_count = 0
consonant_count = 0

vowels = "aeiou"

cons = []
for _char in string.ascii_lowercase:
    # if _char not in "aeiou":
    if _char not in vowels:
        cons.append(_char)

# print(cons)

_consonants = "".join(cons)
# print(_consonants)
##
sentence = input("Please enter a sentence: ")

for char in sentence.lower():
    if char in vowels:
        vowel_count += 1
    elif char in _consonants:
        consonant_count += 1
    elif char == " " or char == ".":
        print("Specials")

print("Vowel count: ", vowel_count)
print("Consonants count: ", consonant_count)
        

