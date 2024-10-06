def floor (x):
  if x >= 0:
    return int(x)  # For positive numbers, just cast to int (this truncates the decimal part)
  else:
    return int(x) - 1 if x != int(x) else int(x)  # For negative numbers, subtract 1 if there's a fractional part
