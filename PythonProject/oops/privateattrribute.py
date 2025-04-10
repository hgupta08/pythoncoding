
#Private attributes can be only accessible from the methods of the class.
# In other words, they cannot be accessible from outside of the class.

class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0

if __name__=="__main__":
    counter = Counter()
    #print(counter.__current) #AttributeError: 'Counter' object has no attribute '__current'
    #also called as name mangling
    # u can only access the variable by objectname._Classname__variable ---so no direct access 
    print(counter._Counter__current)




