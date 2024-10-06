def addition_table_ZN(N):
  # ZN is a set of integers that can be the result of modular N.
  # We generate a 2D list representing the addition table for ZN.
  # The i-th row and j-th column represents (i + j) % N.
  # We use list comprehension to generate this table.
  return [[(i + j) % N for j in range(N)] for i in range(N)]
