import sys
sys.path.insert(0, '/Users/napatcholthaipanich/Dev/master/comp8760_com_sec/lecture/lab')

from pc_1.task2 import floor

def gcd(a, b):
  r1 = a
  s1 = 1
  t1 = 0
  r = b
  s = 0
  t = 1

  while r != 0:
    q = floor(r1 / r)
    r1, r = r, r1 - q * r
    s1, s = s, s1 - q * s
    t1, t = t, t1 - q * t

  d = r1
  x = s1
  y = t1

  return d, x, y

def inverse_list(N):
  z_invest = []
  for i in range(N):
    gcd_value, x_value, y_value = gcd(i, N);
    print(f'gcd({N}, {i}) = {gcd_value} = {y_value} * {N} + {x_value} * {i}')
    if gcd_value == 1:
      print(f'(inverse of {i} = {i})')
      z_invest.append(i)
  print(f'(Z/{N}Z)* = {z_invest}')
  return z_invest
