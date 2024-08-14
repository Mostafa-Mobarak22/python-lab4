class Employee:
    count=0
    def __init__(self,name,id,age,department=None):
        self.name=name
        self.id=id
        self.age=age
        self.department=department
        Employee.count+=1
    def setsalary(self,salary):
        self.salary=salary
        print(f'{self.name} has ${self.salary} ')
    def setdepartment(self,dep):
        self.department=dep
        print(f'{self.name} work in {self.department} department now')