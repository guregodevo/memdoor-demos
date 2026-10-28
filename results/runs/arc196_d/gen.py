import random

def gen():
    N = random.randint(3, 6)
    
    # Generate all valid pairs (s, t) where |s - t| > 1 and s != t
    valid_pairs = []
    for s in range(1, N + 1):
        for t in range(1, N + 1):
            if s != t and abs(s - t) > 1:
                valid_pairs.append((s, t))
    
    random.shuffle(valid_pairs)
    
    M = random.randint(1, min(len(valid_pairs), 4))
    pairs = valid_pairs[:M]
    
    Q = random.randint(1, min(M, 3))
    queries = []
    for _ in range(Q):
        L = random.randint(1, M)
        R = random.randint(L, M)
        queries.append((L, R))
    
    # Print
    print(N, M, Q)
    for s, t in pairs:
        print(s, t)
    for l, r in queries:
        print(l, r)

gen()
