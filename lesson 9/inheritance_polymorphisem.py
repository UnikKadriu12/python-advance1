import math

class Shape:

    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius


    def area(self):
        print( math.pi * self.radius**2)


class Triangle(Shape):
      def __init__(self,base,height):
          self.base = base
          self.height = height

      def area(self):
          print(0.5 *self.base*self.height)


circle = Circle(5)

circle.area()
triangle = Triangle(3,8)

triangle.area()