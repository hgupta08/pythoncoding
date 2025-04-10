filename = "main.py"
if filename.endswith(".py"):
     print("It's a Python file")


print("123abc".isalnum())
#True
print("123abc".isalpha())
#False

print("123456".isdigit())
#True

print("abcdf".islower())
#True

def greet(a="abc",b="def"):
    print(a,b)

greet(a="value")

#Return the Unicode code point for a one-character string.
#only single character
print(ord('a'))
print(ord('z'))
print(ord('&'))
#The chr() method returns a string representing a
# character whose Unicode code point is an integer.


print(chr(33))
#
#
# In this function, you use ord() to determine whether the characters i
# n a string are between 65 and 90, which is the interval of code points
# for uppercase letters, A to Z, in the Unicode table.


def is_uppercase(text):
    for char in text:
        if not (65 <= ord(char) <= 90):
            return False
    return True


is_uppercase("HELLO")


is_uppercase("Hello")

