import sys
from itertools import product

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1
    
    S = []
    T = []
    for i in range(M):
        S.append(int(data[idx])); idx += 1
        T.append(int(data[idx])); idx += 1
    
    queries = []
    for k in range(Q):
        L = int(data[idx]); idx += 1
        R = int(data[idx]); idx += 1
        queries.append((L, R))
    
    num_roads = N - 1
    B = N  # bound for each w_j
    
    for (L, R) in queries:
        found = False
        for w in product(range(-B, B + 1), repeat=num_roads):
            ok = True
            for i in range(L - 1, R):
                s = S[i]
                t = T[i]
                if s < t:
                    roads = list(range(s, t))
                else:
                    roads = list(range(s - 1, t - 1, -1))
                
                total = 0
                for r in roads:
                    total += w[r - 1]
                if total != 0:
                    ok = False
                    break
                
                prefix = 0
                for j in range(len(roads) - 1):
                    prefix += w[roads[j] - 1]
                    if prefix <= 0:
                        ok = False
                        break
                if not ok:
                    break
            
            if ok:
                found = True
                break
        
        print("Yes" if found else "No")

main()
