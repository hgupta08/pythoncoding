class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive):
        super().__init__(name,base_pay)
        # self.name = name
        # self.base_pay = base_pay
        self.sales_incentive = sales_incentive

    def get_pay(self):
        print("child class")
        return self.base_pay + self.sales_incentive
#here get pay in child class is  overriding the parent class

if __name__ == '__main__':
    john = SalesEmployee('John', 5000, 1500)
    print(john.get_pay())
    #
    # jane = Employee('Jane', 5000)
    # print(jane.get_pay())