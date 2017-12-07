"""!@package Shape
This package defines the class Shape to hold area and perimeter information.

More details about shape.
"""

class Shape():
    """!Example shape base class.

    This class is used as an example. It defines simple properties of a shape.
    """
    def __init__(self, area=0, perimeter=0):
        """!Initialize the Shape class.

        You can optionally initialize the class with an area and perimeter.
        These are both initialized to 0 if no arguments are given.

        @param area The area of the shape.
        @param perimeter The perimeter of the shape.
        """
        self.area = area
        self.perimeter = perimeter

    def __repr__(self):
        """repr method to print class

        This is the standard python repr method that tells the interpreter
        how to print this class to the screen.
        """
        return "Area: {0} \nPerimeter: {1}".format(self.area, self.perimeter)

    def setArea(self, area):
        """!Set the area of the shape

        @param area The area to assign to shape.
        """
        self.area = area

    def setPerimeter(self, perimeter):
        """!Set the perimeter of the shape

        @param perimeter The perimeter to assign to shape
        """
        self.perimeter = perimeter

    def getArea(self):
        """!Get the area of the shape.

        @return The area of the shape.
        """
        return self.area

    def getPerimeter(self):
        """!Get the perimeter of the shape.

        @return The perimeter of the shape.
        """
        return self.perimeter
