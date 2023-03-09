#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce

def multiply_list(numbers):
    return reduce((lambda x, y: x * y), numbers)

my_list = [1, 2, 3, 4, 5]
result = multiply_list(my_list)

print("The product of all the numbers in the list is:", result)

