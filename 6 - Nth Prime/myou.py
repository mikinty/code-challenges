from math import sqrt

# memoization yo
mem = [2]

# checks all primes < sqrt(n)
def isPrime(n):
  index = 0
  while mem[index] <= sqrt(n):
    if n % mem[index] == 0:
      return False
    index += 1
  return True # no divisors

# function that finds the nth largest prime
def prime(n):
  if n <= 0: # invalid input
    return None
  elif n <= len(mem): # n > 0
    return mem[n-1]
  else: # add a prime to mem
    start = mem[len(mem) - 1] + 1
    while not isPrime(start):
      start += 1
    mem.append(start)
    return start


if __name__ == '__main__':
  for x in range(1, 26):
    print(prime(x))