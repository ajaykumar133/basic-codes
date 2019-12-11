class Salary:

    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus

class employee:

    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.obj_salary=Salary(pay,bonus)      #this here how composition takes place

    def total_salary(self):
        return self.obj_salary.annual_salary()

emp=employee('aj',20,50000,2000)
print(emp.total_salary())
