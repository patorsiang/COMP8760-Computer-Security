import sys
sys.path.insert(0, '/Users/napatcholthaipanich/Dev/master/comp8760_com_sec/lecture/lab')

from pc_1.task2 import floor

def is_prime (n):
  start_num = 2
  end_num = floor(n**0.5)
  for i in range(start_num, end_num + 1):
    if n % i == 0:
      return False, i
  return True, None

def print_prime(n):
  is_or_not, divider = is_prime(n)
  print(f'Searching for divisors between Results of the 2 and {floor(n**0.5)}')
  if is_or_not:
    print(f'The number {n} is a prime.')
  else:
    print(f'The number {n} is composite with the certificate of compositeness being {divider}.')
