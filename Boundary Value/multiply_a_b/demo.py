import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_calcArea(self):
        self.assertEqual(main.calcArea(250, 1), 250)
        self.assertEqual(main.calcArea(250, 0), "INVALID INPUT")
        self.assertEqual(main.calcArea(250, 2), 500)
        self.assertEqual(main.calcArea(250, 400), 100000)
        self.assertEqual(main.calcArea(250, 401), "INVALID INPUT")
        self.assertEqual(main.calcArea(250, 399),  99750)
        self.assertEqual(main.calcArea(250, 200),  50000)
        self.assertEqual(main.calcArea(1, 200), 200)
        self.assertEqual(main.calcArea(0, 200), "INVALID INPUT")
        self.assertEqual(main.calcArea(2, 200), 400)
        self.assertEqual(main.calcArea(500, 200), 100000)
        self.assertEqual(main.calcArea(499, 200),  99800)
        self.assertEqual(main.calcArea(501, 200), "INVALID INPUT")
        
    def test_calcArea_2(self):
        self.assertEqual(main.calcArea2(250, 1), 250)
        self.assertEqual(main.calcArea2(250, 0), "INVALID INPUT")
        self.assertEqual(main.calcArea2(250, 2), 500)
        self.assertEqual(main.calcArea2(250, 400), 100000)
        self.assertEqual(main.calcArea2(250, 401), "INVALID INPUT")
        self.assertEqual(main.calcArea2(250, 399),  99750)
        self.assertEqual(main.calcArea2(250, 200),  50000)
        self.assertEqual(main.calcArea2(1, 200), 200)
        self.assertEqual(main.calcArea2(0, 200), "INVALID INPUT")
        self.assertEqual(main.calcArea2(2, 200), 400)
        self.assertEqual(main.calcArea2(500, 200), 100000)
        self.assertEqual(main.calcArea2(499, 200),  99800)
        self.assertEqual(main.calcArea2(501, 200), "INVALID INPUT")


if __name__ == '__main__':
    unittest.main()
