"""Test for Shape base class"""
from Shape import Shape

def test_Shape_init_empty():
    shp = Shape()
    assert shp.getArea() == 0 and shp.getPerimeter()== 0

def test_Shape_init_params():
    shp = Shape(2,6)
    assert shp.getArea()== 2 and shp.getPerimeter()== 6

def test_Shape_setArea():
    shp = Shape()
    shp.setArea(2)
    assert shp.getArea()== 2

def test_Shape_setPerimeter():
    shp = Shape()
    shp.setPerimeter(2)
    assert shp.getPerimeter()== 2
