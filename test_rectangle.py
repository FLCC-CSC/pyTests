import pytest
from rectangle import rectangle  # Assuming the class is in a file named rectangle.py

class TestRectangle:
    def test_initialization(self):
        r = rectangle(5, 10)
        assert r.width == 5
        assert r.height == 10
    
    def test_area(self):
        r = rectangle(5, 10)
        assert r.area() == 50
        
        r2 = rectangle(7, 3)
        assert r2.area() == 21
    
    def test_perimeter(self):
        r = rectangle(5, 10)
        assert r.perimeter() == 30
        
        r2 = rectangle(7, 3)
        assert r2.perimeter() == 20
    
    def test_compare(self):
        r1 = rectangle(5, 10)  # Area = 50
        r2 = rectangle(7, 3)   # Area = 21
        r3 = rectangle(5, 10)  # Area = 50
        
        # Test smaller rectangle
        assert r2.compare(r1) < 0
        
        # Test equal rectangles
        assert r1.compare(r3) == 0
        
        # Test larger rectangle
        assert r1.compare(r2) > 0
