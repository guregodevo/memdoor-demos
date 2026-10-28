import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    S = data[1]
    T = data[2]
    
    # Build mapping f; if inconsistent, -1
    f = [-1] * 26
    for s, t in zip(S, T):
        ci = ord(s) - ord('a')
        ti = ord(t) - ord('a')
        if f[ci] == -1:
            f[ci] = ti
        elif f[ci] != ti:
            print(-1)
            return
    
    # Count non-identity edges
    E = 0
    for i in range(26):
        if f[i] != -1 and f[i] != i:
            E += 1
    
    if E == 0:
        print(0)
        return
    
    # Find cycles in the functional graph (non-identity edges only)
    color = [0] * 26  # 0=unvisited, 1=in-current-path, 2=done
    in_cycle = [False] * 26
    C = 0
    
    for start in range(26):
        if f[start] == -1 or f[start] == start:
            continue
        if color[start] != 0:
            continue
        
        path = []
        path_set = {}
        cur = start
        while True:
            if color[cur] == 1:
                # Found a cycle in current path
                idx = path_set[cur]
                for i in range(idx, len(path)):
                    in_cycle[path[i]] = True
                C += 1
                break
            elif color[cur] == 2:
                # Hit previously processed node
                break
            elif f[cur] == -1 or f[cur] == cur:
                # Terminal node, no cycle
                break
            else:
                color[cur] = 1
                path_set[cur] = len(path)
                path.append(cur)
                cur = f[cur]
        
        for node in path:
            color[node] = 2
    
    # Check impossibility: need a free temporary for any cycle
    if C > 0:
        has_free = False
        for z in range(26):
            if f[z] == -1:
                # z doesn't appear in S at all
                has_free = True
                break
            if f[z] != z and not in_cycle[z]:
                # z is a tree node, will be eliminated before we need it
                has_free = True
                break
        if not has_free:
            print(-1)
            return
    
    print(E + C)

solve()
