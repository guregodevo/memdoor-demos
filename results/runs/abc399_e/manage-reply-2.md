### STATUS
continue

### NEXT
Rewrite `solution.py` completely with the following correct algorithm (the current file has a bug — it outputs 4 for input `4\nllem\neeme` where the answer is -1 because the mapping for 'e' is inconsistent: position 2 requires e→m but position 3 requires e→e):

```python
import sys

def solve():
    input = sys.stdin.readline
    N = int(input().strip())
    S = input().strip()
    T = input().strip()
    
    # Step 1: Build mapping f: S-char -> T-char; verify it's a function
    f = {}
    for s, t in zip(S, T):
        if s in f:
            if f[s] != t:
                print(-1)
                return
        else:
            f[s] = t
    
    # Step 2: Build directed graph of non-trivial edges (c -> d where c != d)
    edges = {}
    for c, d in f.items():
        if c != d:
            edges[c] = d
    
    E = len(edges)
    if E == 0:
        print(0)
        return
    
    # Step 3: Count cycles and max cycle length via path-following
    visited = set()
    num_cycles = 0
    max_cycle_len = 0
    
    for start in edges:
        if start in visited:
            continue
        path = []
        pos = {}
        cur = start
        while cur in edges and cur not in visited:
            if cur in pos:
                cycle_len = len(path) - pos[cur]
                num_cycles += 1
                max_cycle_len = max(max_cycle_len, cycle_len)
                break
            pos[cur] = len(path)
            path.append(cur)
            cur = edges[cur]
        for node in path:
            visited.add(node)
    
    # Step 4: A cycle of all 26 letters is impossible (no spare temp)
    if max_cycle_len == 26:
        print(-1)
        return
    
    # Step 5: Answer = (non-trivial edges) + (number of cycles)
    print(E + num_cycles)

solve()
```

After writing the file, run it against all four samples to confirm they pass, then run the stress test to confirm no disagreements with the brute force on the 200 random inputs.

### TASKS
- [done] Build the per-character mapping from S to T; if any character in S maps to two different characters in T, immediately output -1.
- [done] Construct the functional graph on the 26 lowercase letters using only edges where f(c) ≠ c.
- [todo] Rewrite solution.py with the complete correct algorithm: mapping consistency check → build non-trivial edge graph → count cycles via path-following → output E + C (or -1 if cycle of length 26 or inconsistent mapping).
- [todo] Verify all 4 samples pass and the stress test (200 random inputs vs brute force) reports ok.
