import unittest
from original import original_function as tm

input1 = [10, -20, 30, 100, 36]
input2 = [50, 5, 15, -7, 36]
out = [40, 25, 15, 107, 0]

class Tester(unittest.TestCase):
  def setUp(self):
    pass

  def testingvalues(self):
    self.assertEqual(tm(input1[0],input2[0]),out[0])

  def testcase2(self):
    self.assertEqual(tm(input1[1],input2[1]),out[1])

  def testcase3(self):
    self.assertEqual(tm(input1[2],input2[2]),out[2])

  def testcase4(self):
    self.assertEqual(tm(input1[3],input2[3]),out[3])

  def testcase5(self):
    self.assertEqual(tm(input1[4],input2[4]),out[4])


if __name__=='__main__':
  unittest.main()