
"""
    Module to reverse a string either a word or sentence
    using loops and inbuilt methods
"""


sentence = "Python is beautiful"
_reverse = []

# print(len(sentence))
# Using loops
##for c in range(len(sentence)-1, -1, -1):
##    # print(sentence[c])
##    _reverse.append(sentence[c])
##
### print(_reverse)
##
##_revstr = ''.join(_reverse)
##print(_revstr)

##
### Using slicing
_reverse = sentence[::-1]
print(_reverse)
