class Point:

    def __init__(self,a,b):
        self.x=a
        self.y=b

    # def __bool__(self):
    #     if self.x == self.y==0:
    #         return False
    #     else:
    #         return True

if __name__=="__main__":
    p = Point(0,0)
    print(bool(p))

 #by default bool always true for any object so here we are
# overiiding bool to update it to any value we want
