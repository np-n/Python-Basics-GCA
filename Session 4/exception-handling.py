
"""
    Demonstrates exception handling
"""

"""----------------------------------------"""
# Division by zero
##num1 = 5
##num2 = 0
##result = 5/0
##print(result)

### Exception handled for zero division
##num1 = 5
##num2 = 0
##try:
##    result = 5/0
##    print(result)
##except Exception:
##    print("Some error occured")
##except ZeroDivisionError as e:
##    print(e)
##    

"""----------------------------------------"""
# File not found
# f = open('testfile.txt')


try:
    f = open('testfile.txt')
    result = 5/0
    print(result)
##except Exception:
##    print('Error!')
##except Exception as e:
    # print(e)
except FileNotFoundError as e:
    print(e)
except Exception:
    print("Error occured ")

    

