import math
class Point(object):
 
    def __init__(self, x, y):
      
        self.x = x
        self.y = y

    def dist(self,pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
    
p1 = Point(5, 4)
p2 = Point(4, 5)
print(p1.dist(p2))