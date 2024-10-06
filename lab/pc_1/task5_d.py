from task5_c import Z_star_N
def find_all_ai(N):
  z = Z_star_N(N)
  return [[(a ** i) % N for i in range(1, len(z) + 1)] for a in z]
