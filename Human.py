class Human:
    count=0
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        Human.count+=1
    def drink(self,drink):
        print(f"{self.name} drink {drink}")
    def eat(self,eat):
        print(f"{self.name} eat {eat}")
