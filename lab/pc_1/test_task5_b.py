import unittest

from task5_b import find_all_ka

class TestTask5_B(unittest.TestCase):
  def test_z4(self):
    self.assertEqual(find_all_ka(4), [[0, 0, 0, 0], [1, 2, 3, 0], [2, 0, 2, 0], [3, 2, 1, 0]])

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
