import math
class Point(object):
    def __init__(self, x, y):
       
        self.x = x
        self.y = y


    def show(self):
       
        return (self.x, self.y)
    
   
apoint=Point(4,5)
print(apoint.show())
