import unittest

from task4_a import exponent

class TestTask4_A(unittest.TestCase):
  def test_pos(self):
    self.assertEqual(exponent(2, 3), 8)

  def test_0(self):
    self.assertEqual(exponent(2, 0), 1)

  def test_err(self):
    self.assertEqual(exponent(2, -1), "Exponent must be non-negative.")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
