# import counter class from collections module
from collections import Counter

# Creation of a Counter Class object using
# string as an iterable data container
x = Counter("geeksforgeeks")
print(x)

# printing the elements of counter object
for i in x.elements():
    print ( i, end = " ")
a={
    "e":3,
"d":3,
    "c":3



}
counter = Counter(a)
for i in counter.elements():
    print ( i, end = " ")
elements = list(counter.elements())
print(elements)  # Output: ['a', 'a', 'a', 'b', 'b', 'c']