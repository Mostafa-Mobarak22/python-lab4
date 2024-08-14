from Human import Human
from employee import Employee
import dbconnection


human1=Human("mostafa",1223,25)
human1.drink('tea')
human1.eat('fish')
print(human1.count)
human2=Human("aya",5632,35)
human2.drink('milk')
human2.eat('meat')
print(Human.count)
human3=Human("ahmed",9658,22)
human3.drink('coffe')
human3.eat('flafel')
print(Human.count)
human4=Human("mobarak",3201,30)
human4.drink('tea')
human4.eat('fish')
print(human4.count)
# _____________________________________________

emp1=Employee("mostafa",1254,26,"os")
emp1.setsalary(3625)
emp1.setdepartment("java")
print(Employee.count)
emp2=Employee("ahmed",1254,26,"os")
emp2.setsalary(3625)
emp2.setdepartment("java")
print(emp2.count)
# __________________________________________________

