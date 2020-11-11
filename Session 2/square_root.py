"""
    Newton's method for square root
    Given a = 4.0
    x will be a -1 initially

    Afterwards within iteration:
    x = y
    y = (x + a/x) / 2
"""

import math
# Using while loop
count = 10
a = 2256
x = a - 1
while count > 0 :
    y = (x + a/x) / 2
    print(y)
    x = y
    count = count - 1

print()
print(math.sqrt(2256))

### Using for loop
##a = 99.0
##x = a - 1
##for i in range(0, 10):
##    y = (x + a/x) / 2
##    print(y)
##    x = y
##
##print()
##print(math.sqrt(99))
##
##


# Another method
x = 99
x_square_root = x ** 0.5
print(x_square_root)
