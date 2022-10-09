from abc import ABC, abstractmethod


class Shape:
    filled = True
    color = "red"

    def __init__(self, color: str, filled: bool):
        self.color = color
        self.filled = filled

    def Shape(self, color: str, filled: bool):
        print(f"shape is {self.color} and is it filled? {self.filled}")

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, fill):
        self.filled = fill

    @abstractmethod
    def getArea(self) -> int:
        pass

    @abstractmethod
    def getPerimeter(self) -> int:
        pass

    @abstractmethod
    def toString(self) -> str:
        pass


class Circle(Shape):
    def __init__(self, radius: int, color: str, filled: bool):
        super().__init__(color, filled)
        self.radius = radius

    @staticmethod
    def Circles(radius, color: Shape, filled: Shape):
        print(f'radius {radius} , color {Shape.color}, filled or not {Shape.filled}')

    def toString(self) -> str:
        pass

    def getPerimeter(self) -> float:
        return 2 * 3.14 * self.radius

    def getArea(self) -> float:
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    width = 1
    length = 2

    @staticmethod
    def Rectangles(self, color: Shape, filled: Shape):
        print(f'radius {self.width}, length {self.length}, color {Shape.color}, filled or not {Shape.filled}')

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length

    def toString(self) -> str:
        pass

    def getPerimeter(self) -> int:
        return 2 * (self.width + self.length)

    def getArea(self) -> int:
        return self.width * self.length


class Square(Rectangle):
    side = 5

    @staticmethod
    def Rectangles(self, color: Shape, filled: Shape):
        print(f'radius {self.side}, color {Shape.color}, filled or not {Shape.filled}')

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def setWidth(self, width):
        self.width = self.side

    def setLength(self, length):
        self.width = self.side  

