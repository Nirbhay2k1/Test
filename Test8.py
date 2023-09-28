class cyl:
    def __init__(self,h=1,r=1):
        self.h=h
        self.r=r

    def vol(self):
        v = ((22/7) * self.r * self.r * self.h)
        return v
    
    def sa(self):
        s = (((2*(22/7)*self.r) * self.h) + (((22/7)*self.r**2)*2))
        return s
        
c= cyl(2,3)     
print(c.vol())
print(c.sa())   
