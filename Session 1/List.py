
"""-------------------------------------"""
numbers = [1,2,3,4,5,6,7,8,9]
##print("List: ", numbers)
##print("Type: ", type(numbers))
##print("Length: ", len(numbers))

"""-------------------------------------"""
# List methods
numbers.append(10)
print("Before replacing by 100: ", numbers)
numbers[2] = 100 # Lists are mutable
print("After replacing by 100: ", numbers)

print("Before popping out: ", numbers)
print("POP: ", numbers.pop())
print("POP again: ", numbers.pop())
print("List: ", numbers)
print("POP (0): ", numbers.pop(0))
print("List: ", numbers)


print("INSERT at 2: ", numbers.insert(2, 202))
print("List: ", numbers)
print("REMOVE: ", numbers.remove(5))
print("List: ", numbers)

"""-------------------------------------"""
# List addition and append
##list1 = [1,2,3]
##list2 = [4,5,6]
##
##list3 = list1 + list2
##
##print("List1 before append: ", list1)
##list1.append(list2)
##
##print("List3: ", list3)
##print("List1 after append: ", list1)

"""-------------------------------------"""
# List and string
##s = "apple"
##l = list(s) # Breaking a string into list of characters
##print(s)
##print(l)

##s = "blowing in the wind"
##l = s.split()   # Breaking a string to list of words
##print(l)

##l = ["rato", "tika", "nidhar", "ma"]
##s = " ".join(l) # Joining the words with space in between
##print(s)
