import sys
from itertools import permutations

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    S = data[1]
    
    whites = [i + 1 for i in range(2 * N) if S[i] == 'W']
    blacks = [i + 1 for i in range(2 * N) if S[i] == 'B']
    
    count = 0
    MOD = 998244353
    n = 2 * N
    
    for perm in permutations(blacks):
        adj = [[] for _ in range(n + 1)]
        radj = [[] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            adj[i].append(i + 1)
            radj[i + 1].append(i)
        
        for i in range(N):
            adj[whites[i]].append(perm[i])
            radj[perm[i]].append(whites[i])
        
        visited = [False] * (n + 1)
        stack = [1]
        visited[1] = True
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)
        
        ok = True
        for i in range(1, n + 1):
            if not visited[i]:
                ok = False
                break
        if not ok:
            continue
        
        visited2 = [False] * (n + 1)
        stack = [1]
        visited2[1] = True
        while stack:
            v = stack.pop()
            for u in radj[v]:
                if not visited2[u]:
                    visited2[u] = True
                    stack.append(u)
        
        ok = True
        for i in range(1, n + 1):
            if not visited2[i]:
                ok = False
                break
        if not ok:
            continue
        
        count = (count + 1) % MOD
    
    print(count)

solve()
