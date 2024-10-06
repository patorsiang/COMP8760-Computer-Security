import unittest

from task5_d import find_all_ai

class TestTask5_D(unittest.TestCase):
  def test_z_star_5(self):
    self.assertEqual(find_all_ai(5), [[1, 1, 1, 1], [2, 4, 3, 1], [3, 4, 2, 1], [4, 1, 4, 1]])


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
