import sys
from itertools import combinations

def all_pairings(indices):
    """Generate all ways to pair up the given list of indices (must have even length)."""
    if len(indices) == 0:
        yield []
        return
    first = indices[0]
    for i in range(1, len(indices)):
        second = indices[i]
        remaining = indices[1:i] + indices[i+1:]
        for rest in all_pairings(remaining):
            yield [(first, second)] + rest

def solve():
    data = sys.stdin.read().split()
    ptr = 0
    T = int(data[ptr]); ptr += 1
    results = []
    for _ in range(T):
        N = int(data[ptr]); ptr += 1
        K = int(data[ptr]); ptr += 1
        cakes = []
        for i in range(N):
            x = int(data[ptr]); ptr += 1
            y = int(data[ptr]); ptr += 1
            z = int(data[ptr]); ptr += 1
            cakes.append((x, y, z))
        
        best = 0
        for selected in combinations(range(N), 2 * K):
            for pairing in all_pairings(list(selected)):
                total = 0
                for (a, b) in pairing:
                    total += max(cakes[a][0] + cakes[b][0],
                                 cakes[a][1] + cakes[b][1],
                                 cakes[a][2] + cakes[b][2])
                if total > best:
                    best = total
        results.append(best)
    print('\n'.join(str(r) for r in results))

solve()
