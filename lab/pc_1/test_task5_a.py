import unittest

from task5_a import addition_table_ZN

class TestTask5_A(unittest.TestCase):
  def test_z4(self):
    self.assertEqual(addition_table_ZN(4), [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 0, 1, 2]])

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
