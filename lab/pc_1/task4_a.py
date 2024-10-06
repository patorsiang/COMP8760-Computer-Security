def exponent(n, e):
  if e < 0:
    return "Exponent must be non-negative."

  result = 1
  for _ in range(e): # repeat multiply result by number (n)
    result *= n
  return result
