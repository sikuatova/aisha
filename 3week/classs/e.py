class person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age
    def myfunc(abc):
        print("Hello my name is " + abc.name)
        
p1=person("John",36)
p1.myfunc()