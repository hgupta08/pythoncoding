def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError('The second argument (b) must not be zero')


try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
else:
    print('result:', result)