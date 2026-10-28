Looking at this problem, I need to understand the tile rotations and the "no dead ends" condition on a torus, then count valid configurations.

**Key Insight:** For each cell, given its top-edge state, the bottom-edge state is determined by the tile type (flipped for A, same for B). This makes row-to-row transitions deterministic per column, and the torus wraparound requires even A-count per column. The horizontal constraints within each row produce XOR equations on the top-state variables at B-cell positions.

Let me verify my analysis against the samples before writing the solution:
- Sample 1: All columns even A-count, constraint graph gives rank 2 on 3 nodes → 2^(3-2+0) = 2 ✓
- Sample 2: Column 1 has odd A-count → 0 ✓  
- Sample 3: All columns even, constraint graph gives rank 3 on 4 nodes → 2^(4-3+0) = 2 ✓

### STATUS
continue

### NEXT
Write solution.py implementing the following algorithm: (1) For each test case, check every column has even count of 'A' tiles (else answer 0). (2) Count all-A rows; if any exists and W is odd, answer 0. (3) Build a constraint graph on W nodes: for each row with B cells at positions b_0<...<b_{m-1}, for each cyclic consecutive pair (b_k, b_{k+1}), compute gap=(b_{k+1}-b_k-1+W)%W and add undirected edge (b_k, b_{k+1}) with weight gap%2. Special case m==1: if W is even, contradiction (answer 0). (4) BFS on the graph to check consistency (for every edge, color[u]^color[v]==weight) and compute rank = sum of (component_size - 1) over components with edges. (5) Answer = pow(2, W - rank + all_a_count, 998244353). Read input with sys.stdin.buffer.read().split() for speed. Use bytes comparison (row[j]==65 for 'A', row[j]==66 for 'B').

### TASKS
- [todo] Write solution.py with the XOR-constraint-graph algorithm described above and verify against all 3 samples
- [todo] Stress test against a brute force solution on small random cases (H,W ≤ 5)
