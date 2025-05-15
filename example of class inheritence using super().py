

class Shapes:
    def __init__(self, color, is_filled): 
        self.color = color
        self.is_filled = is_filled 


    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shapes):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius 
    
    def describe(self):
        super().describe()
        print(f"It is a cirle with an area of {3.14 * self.radius * self.radius}cm^2")

class Square(Shapes):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width 

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width * self.width}cm^2")


class Triangle(Shapes):
    def __init__(self, color, is_filled, width, hieght):
        super().__init__(color, is_filled)
        self.width = width 
        self.hieght = hieght 

    def describe(self):
        super().describe()
        print(f"It is a cirle with an area of {0.5 * self.width * self.hieght}cm^2")


circle = Circle(color="red", is_filled=True, radius= 5)
square = Square(color="blue", is_filled=False, width= 6)
triangle = Triangle(color="yellow", is_filled=True, width= 6, hieght= 7)



circle.describe()
print()
square.describe()
print()
triangle.describe()

    