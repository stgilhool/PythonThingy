"""Test for square class"""
from Square import Square

def test_Square_init_empty():
    sq = Square()
    assert sq.getSide() == 0

def test_Square_init_params():
    sq = Square(2)
    assert sq.getSide() == 2

def test_Square_Area():
    sq = Square(3)
    assert sq.getArea()==9

def test_Square_Perimeter():
    sq = Square(2)
    assert sq.getPerimeter()==8
