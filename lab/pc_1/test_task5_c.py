import unittest

from task5_c import Z_star_N

class TestTask5_C(unittest.TestCase):
  def test_z_star_2(self):
    self.assertEqual(Z_star_N(2), [1])

  def test_z_star_3(self):
    self.assertEqual(Z_star_N(3), [1, 2])

  def test_z_star_4(self):
    self.assertEqual(Z_star_N(4), [1, 3])

  def test_z_star_12(self):
    self.assertEqual(Z_star_N(12), [1, 5, 7, 11])

  def test_z_star_13(self):
    self.assertEqual(Z_star_N(13), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
