def euclidean_gcd (a, b):
  if b > a:
    a, b = b, a

  # Euclidean algorithm: repeatedly replace a with b and b with the remainder of a divided by b
  while b != 0:
    a, b = b, a % b
  return a
