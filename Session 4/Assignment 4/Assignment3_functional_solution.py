# Implement question number 1, 2 and 6 from Session 3 Exercise as different functions in a single(.py) file

"""
QUESTION:
1.Write a program to display all prime numbers from 1 to 100.

2.Ask the user for a string and print out whether this string is a palindrome or not.
(A palindromeis a string that reads the same forwards and backwards.)


6.Create a dictionary that has a key value pair of letters and the number
of occurrencesof that letter in a string.Given a string “pineapple”.
The result should be as:{“p”:3, “i”:1, “n”:1, “e”:2, “a”:1, “l”:1}
Don’t worry about the order of occurrence of letters.

"""


def display_prime(a,b):
    prime_numbers = []
    for num in range(a,b+1):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    print('Prime numbers are : {}'.format(prime_numbers))




def check_palindrome():
    user_string = input('Enter a string to check it as palindrome or not: ')
    if user_string == user_string[::-1]:
        print('Input string is palindrome')
    else:
        print('Input string is not palindrome')


def str_char_occurance_dict():
    dict_ = {}
    user_string = input('Enter a String : ')
    # Converting to list, each character as list elements
    string_char_list= list(user_string)
    # Getting unique characters
    unique_list_char = set(string_char_list)
    unique_list_char = list(unique_list_char)
    for item in unique_list_char:
        if item == ' ':
            continue
        else:
            dict_[item] = string_char_list.count(item)
    print(dict_)




def main():
    print('*********************************Q1: Display all prime numbers from 1 to 100 **************************************')
    display_prime(1,100)

    print('\n************************Q2: Checking whether the input string is palindrome or not**************************************')
    check_palindrome()

    print('\n**************************Q3: Dictionary having key value pairs as occurance of elements in string************************')
    str_char_occurance_dict()





if __name__ == '__main__':
    main()
