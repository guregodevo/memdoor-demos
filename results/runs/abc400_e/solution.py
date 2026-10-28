import sys
from bisect import bisect_right

def sieve(n):
    """Return list of all primes <= n."""
    is_prime = bytearray(b'\x01') * (n + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray((n - i*i) // i + 1)
    return [i for i in range(2, n + 1) if is_prime[i]]

def main():
    LIMIT = 10**12
    primes = sieve(10**6)
    nprimes = len(primes)

    # Precompute all 400 numbers <= LIMIT
    nums = []
    for i in range(nprimes):
        p = primes[i]
        p2 = p * p
        if p2 * 9 > LIMIT:  # smallest q is 3, q^2=9
            break
        for j in range(i + 1, nprimes):
            q = primes[j]
            q2 = q * q
            if p2 * q2 > LIMIT:
                break
            # Iterate exponents: p^(2a) * q^(2b) <= LIMIT
            pa = p2  # p^(2*1)
            while pa * q2 <= LIMIT:
                qb = q2  # q^(2*1)
                while pa * qb <= LIMIT:
                    nums.append(pa * qb)
                    qb *= q2
                pa *= p2

    nums = sorted(set(nums))

    # Read input and answer queries
    data = sys.stdin.buffer.read().split()
    Q = int(data[0])
    out = []
    for k in range(1, Q + 1):
        A = int(data[k])
        idx = bisect_right(nums, A) - 1
        out.append(str(nums[idx]))
    sys.stdout.write('\n'.join(out) + '\n')

main()
