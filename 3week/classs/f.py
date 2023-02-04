class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+ self.name)
p1=person("Aisha",18)
p1.age=19  
print(p1.age)