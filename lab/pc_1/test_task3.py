import unittest

from task3 import euclidean_gcd

class TestTask3(unittest.TestCase):
  def test_1(self):
    self.assertEqual(euclidean_gcd(539, 1001), 77)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
