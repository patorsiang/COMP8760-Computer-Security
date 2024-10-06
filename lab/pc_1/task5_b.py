def find_all_ka(N):
  # Please find all the results of the addition of a with itself by adding k times and mod with N
  # a is the member of the set of N
  return [[(k * a) % N for k in range(1, N + 1)] for a in range(N)]
