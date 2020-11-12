
"""
    Computes factorial of a number
    5! = 5*4*3*2*1

"""

def factorial(num):
    result = 1
    if num == 0 or num == 1:
        return result
    else:
        for i in range(1, num+1):
            result *= i

    return result


print(factorial(6))
