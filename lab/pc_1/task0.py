def dec_to_bin (n):
  if n == 0: # 1st case: if n is 0, then return 0
    return '0'

  binary = []
  while n > 0:
    binary.insert(0, n%2) # insert only first element like stack array
    n = n // 2
  return ''.join(str(digit) for digit in binary) # return string by joining all elements of binary array
