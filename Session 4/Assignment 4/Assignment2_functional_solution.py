# Implement question number 1, 2 and 4 from Session 2 Exercise as different functions in a single (.py) file.

"""
QUESTIONS:
1.   Choose a list of your choice and find the sum of
all elements of that list.For example, the sum of [6,9,7,5,4] is 31.
Note: You cannot use sum () function here

 2.   Write a program that returns a list which contains common elements
from two lists. Avoid the duplicate elements from lists.
For example a = [1, 1, 3, 5, 7, 9, 9] b = [2, 1, 6 ,9, 2, 1, 3, 5]
The result should be [1, 3, 5, 9]
Note: You cannot use if-else statement here.

4.   Write a code to ask an input from the user which is a string and
display the string along with its length.
Note: You cannot use len () function here.

"""

def sum_list_elements(my_list):
    sum = 0
    for num in my_list:
        sum += num
    return sum


def find_common_elements(a,b):
    # unique list a
    a = set(a)
    b = set(b)
    print(a)
    print(b)
    # a_common_b = a.intersection(b)
    # Alternatively
    a_common_b = a & b
    a_common_b = list(a_common_b)
    print(f'Common elements between list a and b are : {a_common_b}')


def get_string_length(user_string):
    str_len = 0
    for char_ in user_string:
        str_len += 1
    print(f'Length of the your input string {user_string} is :{str_len}')


def main():
    print('*****************Q1: sum of list element without using sum() function*************************')
    my_list = [6,9,7,5,4]
    print(f'Sum of {my_list} list elements is {sum_list_elements(my_list)}')

    print('\n***************************Q2: common elements from the two list ********************************')
    a = [1, 1, 3, 5, 7, 9, 9]
    b = [2, 1, 6 ,9, 2, 1, 3, 5]
    find_common_elements(a,b)

    print('\n**********************************Q4:String length**************************************')
    user_string = input('Enter your favourite string:')
    # Ge get length of string
    get_string_length(user_string)


if __name__ == '__main__':
    main()
