

"""
Exercise 1. Assume that we execute the following assignment statements:
width = 17
height = 12.0
delimiter = '.'

For each of the following expressions, write the value and the typeof the expression.
1.width/2
2.width/2.0
3.height/3
4.1 + 2 * 5
5.delimiter * 5
"""
# Solution:

# 1
# value : 8.5 and type : float

# 2
# value : 8.5 and type : float

# 3
# value : 4.0 and type : float

# 4
# value : 11 and type : int(integer)

# 5
# value : '.....' and type : str(string)

# Source code
width = 17
height = 12.0
delimiter = '.'

print(f"value of expression width/2 is {width/2} and it's type is {type(width/2)}")
print(f"value of expression width/2 is {width/2.0} and it's type is {type(width/2.0)}")
print(f"value of expression width/2 is {height/3} and it's type is {type(height/3)}")
print(f"value of expression width/2 is {1 + 2 * 5} and it's type is {type(1 + 2 * 5)}")
print(f"value of expression width/2 is {delimiter * 5} and it's type is {type(delimiter * 5)}")




""" Exercise 2. Write a program that will convert Fahrenheit to Celsius in degrees """
# solution:

# asking user
# temp_fahrenheit = int(input('Enter temperature in degree Fahrenheit: '))

# or directly assign value
temp_fahrenheit = 200

temp_celsius = (temp_fahrenheit - 32)*(5/9)
print(f'{temp_fahrenheit} degree Fahrenheit equal to {temp_celsius}  degree Celsius')



"""Exercise  3. Write  a  program  that  takes  seconds
as  time  units  and  converts  it  to  minutes  and seconds. """
# solution:

# time_second = int(input('Enter time in seconds: '))
time_seconds = 36

if time_seconds >= 60 :
    minutes = time_seconds // 60
    seconds = time_seconds % 60
else:
    minutes = 0
    seconds = time_seconds

print('\n {} seconds consist of {} minutes and {} seconds'.format(time_seconds,minutes,seconds) )


"""Exercise 4.Consider a list of any arbitrary elements.
Your codeshould print the length of the list and first and fourth element of the list"""
# solution

my_list = [22,3,5,2,5,1,6,44,7,223,645]
# length of list
print('length of list is {}'.format(len(my_list)))
# Alternative
len =0
for x in my_list:
    len = len +1

print(len)
print('First element of list is {}'.format(my_list[0]))
print('Fourth element of list is {}'.format(my_list[4]))





"""Exercise 5.Create a list of any arbitrary elements.
Your code should show the list methods as pop, insert and remove"""
# solution

list_element = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
print(list_element)

# pop() method
# 48 is pop out
list_element.pop()
print(list_element)

# pop 3rd index element from list
list_element.pop(2)
print(list_element)


# insert() method
# Inserting hello in index 1
list_element.insert(1,'hello')
print(list_element)

# remove() method
# Removing element 8 from list
list_element.remove(2)
print(list_element)


s = "apple"
l = list(s) # Breaking a string into list of characters
print(s)
print(l)

name = 'netra prasad neupane'
lst = name.split()
print(lst)



# List addition and append
list1 = [1,2,3]
list2 = [4,5,6]


list1.append(list2)
print(list1)
