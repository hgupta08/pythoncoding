class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    def method(self):
        print(f"Class attribute: {self.class_attr}")
        print(f"Instance attribute: {self.instance_attr}")


if __name__=="__main__":

#accessing class attribute via class
    print(SampleClass.class_attr)
#dict has In a class, .__dict__ will contain class attributes and methods.
# In an instance, .__dict__ will hold instance attributes.


    print(SampleClass.__dict__)

    print(SampleClass.__dict__["class_attr"])
    s=SampleClass("120")
    print(s.__dict__['instance_attr'])


