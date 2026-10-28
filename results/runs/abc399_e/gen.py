import random

def main():
    # Pick a tiny N
    N = random.randint(1, 8)
    
    # Decide alphabet size to create variety of test cases
    r = random.random()
    if r < 0.2:
        # Single letter (trivial)
        alphabet = random.choice('abcdefghijklmnopqrstuvwxyz')
    elif r < 0.45:
        # Two letters
        alphabet = ''.join(random.sample('abcdefgh', 2))
    elif r < 0.7:
        # 3-4 letters
        alphabet = ''.join(random.sample('abcdefghijklmnop', random.randint(3, 4)))
    else:
        # 5+ letters
        alphabet = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(5, 12)))
    
    S = ''.join(random.choice(alphabet) for _ in range(N))
    T = ''.join(random.choice(alphabet) for _ in range(N))
    
    # Sometimes make S == T (answer 0)
    if random.random() < 0.12:
        T = S
    
    # Sometimes make T use a letter not in S's alphabet (forces -1 or interesting cases)
    if random.random() < 0.15 and len(alphabet) < 26:
        extra = random.choice([c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in alphabet])
        pos = random.randint(0, N - 1)
        T = T[:pos] + extra + T[pos+1:]
    
    print(N)
    print(S)
    print(T)

main()
