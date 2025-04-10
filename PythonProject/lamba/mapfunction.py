# The syntax for the map() function is as follows:
#
# map(function, iterable)
#
#
# Parameter:
#
# function: The function we want to apply to every element of the iterable.
# iterable: The iterable whose elements we want to process.

a = [1, 2, 3, 4]

# Using custom function in "function" parameter
# This function is simply doubles the provided number
def double(val):
  return val*2

res = list(map(double, a))
print(res)

a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))


fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))

s = ['  hello  ', '  world ', ' python  ']
res = map(str.strip, s)
print(list(res))


import functools

# Define a list of numbers
numbers = [1, 2, 3, 4]

# Use reduce to compute the product of list elements
product = functools.reduce(lambda x, y: x * y, numbers)
print("Product of list elements:", product)


# Define a function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to filter out even numbers
even_numbers = filter(is_even, numbers)
print("Even numbers:", list(even_numbers))


my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

print(list(filter(lambda name:len(my_names)<7,my_names)))


# Python 3
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)