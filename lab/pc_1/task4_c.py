def exponent(n, e):
  if e < 0:
    return "Exponent must be non-negative."

  result = 1
  base = n
  while e > 0:
    if e % 2 == 1:  # store the result
      result *= base
    base *= base # double itself
    e //= 2
  return result
