from __future__ import annotations
from math import sqrt


class Point:
    """Point in 2D plain"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other: Point) -> float:
        """Calculates distance between self point and other point"""
        delta_x = self.x - other.x
        delta_y = self.y - other.y
        return sqrt(delta_x * delta_x + delta_y * delta_y)

    def __str__(self):
        return f"<{self.x}, {self.y}>"

    def __cmp__(self, other):
        return self.x == other.x and self.y == other.y


class Line:
    """Line with ends A and B"""

    def __init__(self, a: Point, b: Point):
        self.__a = a
        self.__b = b
        # self.length = a.length(b) # not recommended

    @property
    def length(self):
        """calculates line length"""
        return self.__a.distance(self.__b)

    @property
    def a(self):
        """First line end"""
        return self.__a

    @a.setter
    @regex("\w{8,20}")
    def a(self, a: Point):
        self.__a = a

    @property
    def b(self):
        """Second line end"""
        return self.__b

    @b.setter
    def b(self, b: Point):
        self.__b = b

    def __str__(self):
        return f"Line({self.a}, {self.b})"

class ColoredPoint(Point):
    def __init__(self, x: float, y:float, color: str):
        super().__init__(x, y)
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f"<x: {self.x}, y: {self.y}, color: {self._color}>"


if __name__ == "__main__":
    p1 = ColoredPoint(1, 3, "RED")
    p2 = ColoredPoint(4, 6, "BLUE")
    print(f"Distance between {p1} and {p2} is: {p1.distance(p2)}")
    l1 = Line(p1, p2)
    # print(f"Line between {l1._Line__a} and {l1._Line__b}")
    print(f"Line between {l1.a} and {l1.b}")  # RVal a & b properties
    print(f"{l1} length is: {l1.length}") # RVal length property
    l1.a = ColoredPoint(0, 0, "RED")  # LVal a property
    print(f"\nAfter change\nLine between {l1.a} and {l1.b}")
    print(f"{l1} length is: {l1.length}")
    # print(help(Line))
