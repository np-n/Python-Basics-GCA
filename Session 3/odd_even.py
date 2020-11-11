
"""
    Stores all even numbers and odd numbers from 1 to 30
    in different lists
"""

even_numbers = []
odd_numbers = []

for num in range(1, 30):
    # print(num)
    if num%2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)


print("Odd numbers till 30: ", odd_numbers)
print("Even numbers till 30: ", even_numbers)
