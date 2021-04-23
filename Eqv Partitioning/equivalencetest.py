# a : 1 -> 20
# b : 0 -> 20 
# CLASSES
# A1 = a<1
# A2 = a>=1 && a<=20
# A3 = a>20
# B1 = b<0
# B2 = b>=0 && b<=20
# B3 = b>20
# test module

import unittest
import equivalence


class TestingMain(unittest.TestCase):
    def test_power1(self):
        self.assertEqual(equivalence.power1(5,5),3125)
        self.assertRaises(ValueError,equivalence.power1,5,-1)
        self.assertRaises(ValueError,equivalence.power1,5,21)
        self.assertRaises(ValueError,equivalence.power1,0,5)
        self.assertRaises(ValueError,equivalence.power1,21,5)

    def test_power2(self):
        self.assertEqual(equivalence.power2(5,5),3125)
        self.assertRaises(ValueError,equivalence.power2,5,-1)
        self.assertRaises(ValueError,equivalence.power2,5,21)
        self.assertRaises(ValueError,equivalence.power2,0,5)
        self.assertRaises(ValueError,equivalence.power2,21,5)

# to run all the test
if __name__ == '__main__':
    unittest.main()