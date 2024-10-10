import random
from task1_a import is_prime

def primes_arr_between_1_and_100():
    primes = []
    for num in range(2, 101):
        if is_prime(num):
            primes.append(num)
    return primes

def is_prime_by_partial_trials_division(n):
  for i in primes_arr_between_1_and_100():
    if n % i == 0 and i != n:
      return 0, i
  return 1, None

def is_prime_by_fermat_primality_test(n, k):
  for _ in range(k):
    a = random.randint(2, n - 1)
    if (a ** (n-1)) % n != 1:
      return False, a  # Return False with certificate of compositeness
  return True, None

def is_prime_by_test (n, k):
  # Step 1: Partial trial division with primes < 100
  is_prime, divisor = is_prime_by_partial_trials_division(n)
  print('Searching for divisors only among primes between 2 and 97')
  if not is_prime:
    print(f'The number {n} is composite with the certificate of compositeness being {divisor}.')
    return 0

  # Step 2: Fermat's primality test with k iterations
  print(f'Running Fermat\'s test for k={k} iterations')
  is_prime, witness = is_prime_by_fermat_primality_test(n, k)
  if is_prime:
    print(f'The number {n} is probably prime (verified with partial trail division with prime numbers less than 100 and with Fermat\'s test with {k} iterations)')
  else:
    print(f'The number {n} is composite with the certificate of compositeness being {witness}.')
  return 1  # Return the probably prime number

def generate_probable_prime(k=50):
  while True:
    p = random.randint(100000, 999999)  # Generate a random 6-digit number
    print(f'Checking for n={p}')
    # Step 1: Partial trial division with primes < 100
    is_prime = is_prime_by_partial_trials_division(p)
    print('Searching for divisors only among primes between 2 and 97')
    if not is_prime:
      continue  # If divisible by a prime < 100, try again

    # Step 2: Fermat's primality test with k iterations
    print(f'Running Fermat\'s test for k={k} iterations')
    is_prime = is_prime_by_fermat_primality_test(p, k)
    if is_prime:
      print(f'The number {p} is probably prime (verified with partial trail division with prime numbers less than 100 and with Fermat\'s test with {k} iterations)')
      return p  # Return the probably prime number

if __name__ == '__main__':
  generate_probable_prime()
