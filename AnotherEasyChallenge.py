from math import pi 

class Circle:

    def __init__(self, radius = 1.0, color = "red"):
        self._radius = float(radius)
        self._color = str(color) 


    def getRadius(self):
        return self._radius
    

    def setRadius(self,radius):
        self._radius=radius
    

    def getColor(self):
        return self._color
    

    def setColor(self,color):
        self._color=color
    
    def __str__(self):
        return(f'radius= {self.getRadius()}, color= {self.getColor()}')
    
    def getArea(self):
        return (math.pi * self.getRadius()**2)


class Cylinder(Circle):

    def __init__(self, height = 1.0, radius = 1.0, color = "red"):
        super().__init__(radius, color)
        self.__height = height
        
    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def __str__(self):
        return (f'radius= {self.getRadius()}, color= {self.getColor()},height= {self.getHeight()}')

    def getVolume(self):
        return (self.getArea() * self.__height)

circle = Circle()
cylinder = Cylinder()