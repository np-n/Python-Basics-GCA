# Q1 : Implement question number 2, 3, 4 and 5 from Session 1 Exercise as different functions in a single file.


"""
QUESTIONS:

Exercise 2. Write a program that will convert Fahrenheit to Celsius in degrees.

Exercise  3. Write  a  program  that  takes  seconds  as  time  units  and  converts  it  to  minutes  and seconds.
For example: 3800 seconds results in 63 minutes and 20 seconds.

Exercise 4.Consider a list of any arbitrary elements.
Your code should print the length of the list and first and fourth element of the list.

Exercise 5.Create a list of any arbitrary elements.
 Your code should show the list methods as pop, insert and remove.

"""

def fahrenheit_to_celsius():
    # Asking user degree in Fahrenheit
    fahrenheit = float(input('Enter degree in fahrenheit to convert celsius: '))
    celsius  = (fahrenheit - 32)*(100/180)
    print(f'{fahrenheit} degree is equal to {round(celsius,4)} degree.')



def seconds_converter():
    seconds_ = int(input('Enter seconds : '))
    # In default minutes and seconds are assigned to zero
    minutes = 0
    seconds = 0
    # Converting seconds to minutes and seconds
    minutes = seconds_// 60
    seconds = seconds_% 60
    print(f'{seconds_} consists of {minutes} minutes and {seconds} seconds. ')


def list_analyser():
    my_list = ['hello','I','am','Netra','Prasad','Neupane']
    print(f'Length of the {my_list} is {len(my_list)}')
    print(f'First element of the list is {my_list[0]}')
    print(f'Fourth element of the list is {my_list[3]}')


def list_methods():
    my_list = ['hello','I','am','Netra','Prasad','Neupane']
    print(f'My list is {my_list}')
    # pop() methods removes/pop last element from the list as default
    # pop third element from list
    popped_element = my_list.pop(2)
    print(f'After popping {popped_element} element list becomes {my_list}')
    # insert() method takes first argument as index and second argument as element to insert
    # insert 6  to 5th index
    my_list.insert(5, 6)
    print(f'After inserting 6 string list becomes {my_list}')
    # remove() method removes the given argument from the list
    # remove string 'I'string from the list
    my_list.remove('I')
    print(f'After removing I list becomes {my_list}')








def main():
    print('********** Q2 : Converting Fahrenheit to Celsius*****************')
    fahrenheit_to_celsius()

    print('\n********** Q3 : Converting Seconds to minutes and seconds *****************')
    seconds_converter()

    print('\n************** Q4 : Converting Seconds to minutes and seconds *****************')
    list_analyser()

    print('\n************** Q5 : List methods: pop,remove,insert *****************')
    list_methods()


if __name__ == "__main__":
    main()
