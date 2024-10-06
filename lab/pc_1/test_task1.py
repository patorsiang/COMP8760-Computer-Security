import unittest

from task1 import list_all_n_bits_values

class TestTask1(unittest.TestCase):
  def test_1_bits(self):
    self.assertEqual(list_all_n_bits_values(1), ['0', '1'])

  def test_2_bits(self):
    self.assertEqual(list_all_n_bits_values(2), ['00', '01', '10', '11'])

  def test_3_bits(self):
    self.assertEqual(list_all_n_bits_values(3), ['000', '001', '010', '011', '100', '101', '110', '111'])

  def test_0_bits(self):
    self.assertEqual(list_all_n_bits_values(0), "Invalid input. Please enter a number between 1 and 25.")

  def test_26_bits(self):
    self.assertEqual(list_all_n_bits_values(26), "Invalid input. Please enter a number between 1 and 25.")


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
