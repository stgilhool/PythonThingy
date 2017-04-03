"""!square
An implementation of shape.

This implements the shape base class as a square
"""
from Shape import Shape

class Square(Shape):
    """!Square class.

    Inherits from Shape.
    """

    def __init__(self, side=0):
        """!Initialize square with a side length

        @param side The length of one side of a square
        """
        self.side = side

    def setSide(self, side):
        """!Set the length of a side.

        @param side The length of the side of a square
        """
        self.side = side

    def getSide(self):
        """!Get the length of the side.

        @return The length of the side of the square.
        """
        return self.side

    def setArea(self, area):
        """!Overwrite base function to disable.

        We dont want to be able to set the area manually in a square, so we dissable the function.
        """
        raise AttributeError('You cannot set the area manually in the square class. Use setSide instead.')

    def setPerimeter(self, perimeter):
        """!Overwrite base function to disable.

        We dont want to be able to set the perimeter manually in a square, so we dissable the function.
        """
        raise AttributeError('You cannot set the perimeter manually in the square class. Use setSide instead.')

    def getArea(self):
        """!Get the area of the square.

        @return The area of the square.
        """
        return self.side * self.side

    def getPerimeter(self):
        """!Get the perimeter of the square.

        @return The perimeter of the square.
        """
        return self.side * 4
