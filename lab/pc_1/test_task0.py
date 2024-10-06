import unittest

from task0 import dec_to_bin

class TestTask0(unittest.TestCase):
  def test_0(self):
    self.assertEqual(dec_to_bin(0), '0')

  def test_1(self):
    self.assertEqual(dec_to_bin(1), '1')

  def test_2(self):
    self.assertEqual(dec_to_bin(2), '10')

  def test_3(self):
    self.assertEqual(dec_to_bin(3), '11')

  def test_4(self):
    self.assertEqual(dec_to_bin(4), '100')

  def test_5(self):
    self.assertEqual(dec_to_bin(5), '101')

  def test_6(self):
    self.assertEqual(dec_to_bin(6), '110')

  def test_7(self):
    self.assertEqual(dec_to_bin(7), '111')

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
