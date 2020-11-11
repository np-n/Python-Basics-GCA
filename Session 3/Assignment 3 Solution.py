"""1.Write a program to display all prime numbers from 1 to 100."""

# Solution:

prime_numbers = []
for num in range(1,101):
    a = 1
    if num > a:
        for i in range(a+1,num):
            if(num % i) == 0:
                break
        else:
            prime_numbers.append(num)

print(prime_numbers)




"""2.Ask the user for a string and print out whether this string is a palindrome or not.
(Apalindromeis a string that reads the same forwards and backwards.)"""

# Solution:

user_input = input('Enter a string: ')
user_input = user_input.lower()
if user_input == user_input[::-1]:
    print('String is palindrome')
else:
    print('String is not palindrome')





"""3.Given a string, count all lower case, upper case, digits and special symbols"""

# solution:

string_ = 'What is 001 @'
str_list = list(string_)
print(str_list)
lower_char =0
upper_char =0
digits =0
special_char =0
for item in str_list:
    if item is not ' ':
        if item.isupper():
            upper_char += 1
        elif item.islower():
            lower_char +=1
        elif item.isdigit():
            digits +=1
        else:
            special_char +=1


print('Uppercase :',upper_char)
print('Lowercase :',lower_char)
print('Digits :',digits)
print('Special character:',special_char)



"""Write a program to display the n terms of harmonic series and their sum.
1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n """

# solution:

# Asking user for n variable
n = int(input("Enter number of terms n: "))
sum = 0
for i in range(1,n+1):
    sum = sum + (1/i)
print("The sum of series is",sum)




"""5.Write a program to display the following pattern.
 Check also with different number of rows.
     *
    **
   ***
  ****
 *****"""

 # Solution


for row in range(1, 5+1):
    # For white space
    for space in range (1, (5-row)+1):
        print(" ", end="")
    # for symbol
    for symbol in range(1, row+1):
        print("*", end="")

    print ()


# Alternative way
row =5
for i in range(row,-1,-1):
        for j in range(i):
            print(" ",end =" ")

        for k in range(row-i):
            print("*", end = " ")
        print()




"""6.Create a dictionary that has a key value pair of letters
and the number of occurrencesof that letter in a string.
Given a string “pineapple”. The result should be as:
{“p”:3, “i”:1, “n”:1, “e”:2, “a”:1, “l”:1}
Don’t worry about the order of occurrence of letters."""

# Solution


def create_occurance_dict(string):
    if len(string) >= 1 and str_input_ !=" ":
        print(type(string))
        # Converting to list
        string_char_list = list(string)
        print(string_char_list)
        # converting list to sets to get unique characters
        string_char_set = set(string_char_list)
        print(string_char_set)
        dict_ = dict()

        for item in string_char_set:
            # To avoiding whitespace and tab counting
            if item == " " or item == "\t":
                continue
            # counting unique characters in list and storing
            # dictionary as key value pairs
            dict_[item] = string_char_list.count(item)
        print(dict_)

    else:
        print('Enter valid input string')

str_input_ = input('Enter string: ')
create_occurance_dict(str_input_.lower())

# Alternative
char_ = 'pineapple'
for i in range(len(char_)):
    if len(char_) == 0:
      break;
    ch = char_[0]
    if ch == ' ' or ch == '\t':
      continue
    result= ({ch :  char_.count(ch)})
    print (dict(result))
    char_ = char_.replace(ch, '').strip()



