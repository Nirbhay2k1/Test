import math
class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        p1=self.coor1
        p2=self.coor2
        print(math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ))

    def slope(self):
        x1 = self.coor1[0]
        x2 = self.coor2[0]
        y1 = self.coor1[1]
        y2 = self.coor2[1]
        if(x2 - x1 != 0):
            print( (float)(y2-y1)/(x2-x1))
        
coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
li.distance()
li.slope()
