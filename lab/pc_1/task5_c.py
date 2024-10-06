from task3 import euclidean_gcd

def Z_star_N(N):
  # Find all integers x in the set Z*N such that their greatest common divisor with N is 1
  return [x for x in range(1, N) if euclidean_gcd(x, N) == 1]
