def list_all_n_bits_values (n):
  # bin(i) -> 0b***
  # [2:] -> remove the '0b' prefix
  # zfill(n) -> add leading zeros to make the binary string of length n
  # list comprehension -> generate a list of binary strings of length n with 'n' bits
  if n <= 25 and n > 0:
    return [bin(i)[2:].zfill(n) for i in range(2**n)]
  else:
    return "Invalid input. Please enter a number between 1 and 25."
