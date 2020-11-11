#****** Q5:************


# Soln
row =5
for i in range(row,-1,-1):
        for j in range(i):
            print(" ",end =" ")

        for k in range(row-i):
            print("*", end = " ")
        print()



# p1
def display_pattern(row):
    for i in range(row):
        for j in range(i+1):
            print('*',end =" ")
        print()
display_pattern(5)

print()

# p2
def display_pattern(row):
    for i in range(row,-1,-1):
        for j in range(i):
            print('*',end =" ")
        print()

display_pattern(5)


# p 3
row =5
for i in range(row):
    for j in range(i+1):
        print('*',end =" ")
    print()

for i in range(row,-1,-1):
        for j in range(i):
            print('*',end =" ")
        print()


# ********************Q6*****************

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
