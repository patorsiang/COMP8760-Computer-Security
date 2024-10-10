import sys
sys.path.insert(0, '/Users/napatcholthaipanich/Dev/master/comp8760_com_sec/lecture/lab')

from pc_1.task2 import floor

def gcd(a, b):
  print("--------------------------------")
  print(f'a = {a}, b = {b}')
  print("Initialising:")
  r1 = a
  s1 = 1
  t1 = 0
  r = b
  s = 0
  t = 1
  print(f'r1 = {r1}, s1 = {s1}, t1 = {t1}, \t r1 = s1 * a +t1 * b = {s1}  * {a} + {t1} * {b} = {r1}')
  print(f'r = {r}, s = {s}, t = {t}, \t r = s * a +t * b = {s}  * {a} + {t} * {b} = {r}')

  while r != 0:
    print("--------------------------------")
    q = floor(r1 / r)
    print(f'q = floor({r1}/{r}) = {q}')
    print(f'r = {r1 - q * r} = {r1} - {q} * {r}')
    r1, r = r, r1 - q * r
    print(f's = {s1 - q * s} = {s1} - {q} * {s}')
    s1, s = s, s1 - q * s
    print(f't = {t1 - q * t} = {t1} - {q} * {t}')
    t1, t = t, t1 - q * t

  d = r1
  x = s1
  y = t1

  print("--------------------------------")

  return d, x, y
