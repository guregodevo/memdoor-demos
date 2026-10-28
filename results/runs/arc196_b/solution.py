import sys
from collections import deque

MOD = 998244353

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []
    
    for _ in range(T):
        H = int(data[idx]); W = int(data[idx+1]); idx += 2
        grid = []
        for i in range(H):
            grid.append(data[idx])
            idx += 1
        
        # Check row parity (each row must have even number of A's)
        ok = True
        for i in range(H):
            cnt = 0
            row = grid[i]
            for j in range(W):
                if row[j] == 65:
                    cnt += 1
            if cnt & 1:
                ok = False
                break
        if not ok:
            out.append('0')
            continue
        
        # Check column parity (each column must have even number of A's)
        for j in range(W):
            cnt = 0
            for i in range(H):
                if grid[i][j] == 65:
                    cnt += 1
            if cnt & 1:
                ok = False
                break
        if not ok:
            out.append('0')
            continue
        
        # row_xor[i][j] = a(i,1)^a(i,2)^...^a(i,j) for j>=1, 0 for j=0
        row_xor = [[0]*W for _ in range(H)]
        for i in range(H):
            row = grid[i]
            for j in range(1, W):
                row_xor[i][j] = row_xor[i][j-1] ^ (1 if row[j] == 65 else 0)
        
        # col_xor[i][j] = a(1,j)^a(2,j)^...^a(i,j) for i>=1, 0 for i=0
        col_xor = [[0]*W for _ in range(H)]
        for j in range(W):
            for i in range(1, H):
                col_xor[i][j] = col_xor[i-1][j] ^ (1 if grid[i][j] == 65 else 0)
        
        # Build constraint graph on H+W nodes
        # Node i (0<=i<H) represents R_i (free var for row i horizontal)
        # Node H+j (0<=j<W) represents C_j (free var for col j vertical)
        n = H + W
        adj = [[] for _ in range(n)]
        
        for i in range(H):
            row = grid[i]
            for j in range(W):
                if row[j] == 66:  # 'B'
                    pj = j - 1 if j > 0 else W - 1
                    qi = i - 1 if i > 0 else H - 1
                    d = 1 ^ row_xor[i][pj] ^ col_xor[qi][j]
                    u = i
                    v = H + j
                    adj[u].append((v, d))
                    adj[v].append((u, d))
        
        # BFS for consistency check and rank computation
        color = [-1] * n
        rank = 0
        consistent = True
        
        for start in range(n):
            if color[start] != -1:
                continue
            color[start] = 0
            q = deque([start])
            comp_size = 0
            
            while q and consistent:
                u = q.popleft()
                comp_size += 1
                for v, w in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ w
                        q.append(v)
                    elif color[v] != color[u] ^ w:
                        consistent = False
                        break
            
            if not consistent:
                break
            
            if comp_size > 1:
                rank += comp_size - 1
        
        if not consistent:
            out.append('0')
        else:
            free_vars = n - rank
            out.append(str(pow(2, free_vars, MOD)))
    
    sys.stdout.write('\n'.join(out) + '\n')

solve()
