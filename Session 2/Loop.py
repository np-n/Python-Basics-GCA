"""-----------------------------------------"""
### While loop example
##num = 0   # initial value
##while num < 5:
##    print(num)
##    # num = num + 1
##
##    num += 1 # num += 1 equals num = num + 1



"""-----------------------------------------"""
### Using for loop
##for num in range(0, 10):
##    print(num)


"""-----------------------------------------"""
# Further loops
# Prints out the numbers 0,1,2,3,4
##for x in range(5):
##    print(x, end=" ")
##print() # Print itself leads to a newline
##
##### Prints out 3,4,5
##for x in range(3, 6):
##    print(x, end=" ")
##print()
####
##### Prints out 3,5,7
##for x in range(3, 7, 2):
##    print(x, end=" ")

"""-----------------------------------------"""
# Using loop with list
example = list()    # Create an empty list
for num in range(0, 10, 2):
    example.append(num ** 2)

print(example)

for item in example:
    print(item)

