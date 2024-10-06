def exponent(n, e):
  if e < 0:
    return "Exponent must be non-negative."
  elif e == 0:
    return 1
  elif e == 1:
    return n
  elif e % 2 == 0:
    half = exponent(n, e / 2)
    return half * half
  else:
    half = exponent(n, (e - 1) / 2)
    return n * half * half
