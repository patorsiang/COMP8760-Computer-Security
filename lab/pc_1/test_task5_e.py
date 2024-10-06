import unittest

from task5_e import multiplication_table_Z_star_N

class TestTask5_E(unittest.TestCase):
  def test_z_star_5(self):
    self.assertEqual(multiplication_table_Z_star_N(5), [[1, 2, 3, 4], [2, 4, 1, 3], [3, 1, 4, 2], [4, 3, 2, 1]])


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
