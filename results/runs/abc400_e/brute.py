def prime_factors_with_exponents(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                count += 1
                n //= d
            factors.append((d, count))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return factors

def is_400_number(n):
    factors = prime_factors_with_exponents(n)
    if len(factors) != 2:
        return False
    for p, e in factors:
        if e % 2 != 0:
            return False
    return True

import sys
data = sys.stdin.read().split()
Q = int(data[0])
queries = [int(data[i + 1]) for i in range(Q)]

for A in queries:
    for candidate in range(A, 35, -1):
        if is_400_number(candidate):
            print(candidate)
            break
