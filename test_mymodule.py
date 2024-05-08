import unittest
from mymodule import square, double, add

# Test cases for the square function
class TestSquare(unittest.TestCase): 
    def test1(self): 
        # Test when 2 is given as input, the output is 4.
        self.assertEqual(square(2), 4) 
        # Test when 3.0 is given as input, the output is 9.0.
        self.assertEqual(square(3.0), 9.0)  
        # Test when -3 is given as input, the output is not -9.
        self.assertNotEqual(square(-3), -9)  

# Test cases for the double function
class TestDouble(unittest.TestCase): 
    def test1(self): 
        # Test when 2 is given as input, the output is 4.
        self.assertEqual(double(2), 4) 
        # Test when -3.1 is given as input, the output is -6.2.
        self.assertEqual(double(-3.1), -6.2) 
        # Test when 0 is given as input, the output is 0.
        self.assertEqual(double(0), 0) 

# Test cases for the add function
class TestAdd(unittest.TestCase): 
    def test1(self): 
        # Test addition of 2 and 4, the result should be 6.
        self.assertEqual(add(2, 4), 6) 
        # Test addition of 0 and 0, the result should be 0.
        self.assertEqual(add(0, 0), 0) 
        # Test addition of 2.3 and 3.6, the result should be 5.9.
        self.assertEqual(add(2.3, 3.6), 5.9) 
        # Test concatenation of "hello" and "world", the result should be "helloworld".
        self.assertEqual(add("hello", "world"), "helloworld") 
        # Test addition of 2.3000 and 4.300, the result should be 6.6.
        self.assertEqual(add(2.3000, 4.300), 6.6) 
        # Test addition of -2 and -2, the result should not be 0.
        self.assertNotEqual(add(-2,-2), 0)
