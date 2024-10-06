from task5_c import Z_star_N

def multiplication_table_Z_star_N(N):
  z = Z_star_N(N)
  return [[(a * b) % N for b in z] for a in z]
