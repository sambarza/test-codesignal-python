import unittest
from solution import house_game
 
class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(house_game([123, 234, 345, 456]), [362, 433, 144, 255])
 
    def test2(self):
        self.assertEqual(house_game([12, 34, 56]), [41, 63, 25])
 
    def test3(self):
        self.assertEqual(house_game([1, 2]), [2, 1])
 
    def test4(self):
        self.assertEqual(house_game([141, 4]), [44, 11])
 
    def test5(self):
        self.assertEqual(house_game([155, 261, 31]), [15, 156, 123])
 
    def test6(self):
        self.assertEqual(house_game([1, 1, 2, 2, 3, 3]), [3, 1, 1, 2, 2, 3])
 
    def test7(self):
        self.assertEqual(house_game([111, 222, 333]), [231, 312, 123])
 
    def test8(self):
        self.assertEqual(house_game([5]*5), [5]*5)
 
if __name__ == '__main__':
    unittest.main()