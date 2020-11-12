
"""
    mininum and maximum of three numbers
"""

def max_three(num1, num2, num3):
    _max = 0
    if num1 >= num2 and num1 >= num3:
        _max = num1

    elif num2 >= num3 and num2 >= num1:
        _max = num2

    else:
        _max = num3

    return _max

# Minimum would be change with less than sign


