import unittest

from task2 import floor

class TestTask2(unittest.TestCase):
  def test_pos_int(self):
    self.assertEqual(floor(20), 20)

  def test_float(self):
    self.assertEqual(floor(20/7), 2)

  def test_float_0(self):
    self.assertEqual(floor(20/27), 0)

  def test_neg_float(self):
    self.assertEqual(floor(-20/7), -3)

  def test_neg_int(self):
    self.assertEqual(floor(-20), -20)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
