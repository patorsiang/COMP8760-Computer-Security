import unittest

from task4_b import exponent

class TestTask4_B(unittest.TestCase):
  def test_odd(self):
    self.assertEqual(exponent(2, 3), 8)

  def test_even(self):
    self.assertEqual(exponent(2, 2), 4)

  def test_zero(self):
    self.assertEqual(exponent(2, 0), 1)

  def test_err(self):
    self.assertEqual(exponent(2, -1), "Exponent must be non-negative.")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
