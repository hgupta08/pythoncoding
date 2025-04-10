name="asda"
a="ss"
message = f'Hi {name} {a}'
print(message)

words = ["Time", "flies", "like", "an", "arrow!"]
print("h".join(words))


#use llist comprensshension

countdown = [3, 2, 1]
print("-".join(str(number) for number in countdown))

#ternanry operator
age=10

if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5

ticket_price = 5 if int(age) >= 18 else 20  #ternary operator
#value_f_true if <condition> else <value if false>

g= reversed("heelo")
print(next(g))  # will give last chracter

print("".join(reversed("Hello, World!")))


# Using .join() is the recommended approach to concatenate strings in Python.
#It’s clean, efficient, and Pythonic.
print(r"Hello\nWorld")  # r ingore \n and it prints it as a whole
#r can help in defining path
path1 = "C:\\Users\\Real Python\\main.py"
path2 = r"C:\Users\Real Python\main.py"



for index in range(10):
    print(index)
    if index % 2:
        print("inside loop")
        print(f"printing {index} % 2 is  {index % 2}")
        continue

    print(index)

