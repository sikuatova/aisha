
class Point(object):
  

    def __init__(self, x, y):
     
        self.x = x
        self.y = y


    def show(self):
     
        return (self.x, self.y)


    def move(self, x, y):
    
        self.x += x
        self.y += y
p1=Point(4,5)
p1.move(10, -10)
print(p1.show())