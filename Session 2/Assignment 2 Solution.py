"""1.   Choose a list of your choice and find the sum of all elements of that list.
 For example,
 the sum of [6,9,7,5,4] is 31.
 Note: You cannot use sum () function here"""

#Soluton:
my_list = [2,45,5,6,2]
sum = 0
for i in my_list:
    sum = sum + i


print(f'Sum of list {my_list} is {sum}')



"""2.   Write a program that returns a list which contains common elements from two lists. Avoid the duplicate elements from lists.
 For example
 a = [1, 1, 3, 5, 7, 9, 9]
 b = [2, 1, 6 ,9, 2, 1, 3, 5]
 The result should be [1, 3, 5, 9]
Note: You cannot use if-else statement here.
"""

# Solution

a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6 ,9, 2, 1, 3, 5]
# Converting to sets to get unique elements
a_unique = set(a)
b_unique = set(b)
common_elements = a_unique & b_unique
common_elements = list(common_elements)
print(f'common elements from two list {a} and {b} are {common_elements}')


# Alternative approach without using set
"""a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6 ,9, 2, 1, 3, 5]
# converting list to unique list
a_unique = list()
b_unique = list()

for x in a:
    # check if exist in unique list or not
    if x not in a_unique:
        a_unique.append(x)

for x in b:
    if x not in b_unique:
        b_unique.append(x)

print(a_unique)
print(b_unique)

common_elements = list()
for i in a_unique:
    for j in b_unique:
        if i ==j:
            common_elements.append(i)
print(common_elements)"""



"""3.   Suppose you have a list [1, 5, 7, 12 ,15]
Print each number using loop.
Also, print the square of each number using loop."""

my_list = [1, 5, 7, 12 ,15]

# Print number using for loop
print('Printing numbers:')
for num in my_list:
    print(num)

# Print square of numbers using list
print('Printing square of numbers:')
for num in my_list:
    print(num ** 2)


"""4.   Write a code to ask an input from the user which is a string and display the string along with its length.
Note: You cannot use len () function here. """

user_string = input('Enter your favourite string to count length:')
str_length = 0
for i in user_string:
    str_length += 1

print(f'Your string input is {user_string} and length of your string is {str_length}\n')



"""5.   Write a code to ask an input from the user which is a string and convert it to uppercase and lowercase."""

user_input_ = input('Enter String to convert uppercase and lowercase:')
print(f'Your input string is {user_input_}')
print('Coverting your input to:')
print(f'Uppercase: {user_input_.upper()}')
print(f'lowercase: {user_input_.lower()}')
