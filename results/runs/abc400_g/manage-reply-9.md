### STATUS
continue

### NEXT
Completely rewrite solution.py with the correct algorithm: For each test case, try all 3 sort orders (by X desc, Y desc, Z desc). For each sort order, compute the N-1 adjacent-pair values v[i] = max(X_i+X_{i+1}, Y_i+Y_{i+1}, Z_i+Z_{i+1}), then use a max-heap + doubly-linked-list "undo" algorithm to select K non-adjacent elements maximizing the sum. The answer is the maximum across the 3 sort orders. The select_k_nonadjacent algorithm: maintain a doubly linked list and a max-heap with version numbers; each step pops the max element i, adds its value to the answer, removes i and its neighbors L,R from the list, and if both L and R existed, inserts a new element at position i with value val[L]+val[R]-val[i] (the "undo" option) and pushes it into the heap. Handle boundary cases where L or R is -1 (just remove without inserting a new element). Use version numbers to skip stale heap entries.

Here is the complete correct solution to use:

```python
import sys
import heapq

def select_k_nonadjacent(vals, K):
    M = len(vals)
    if K == 0 or M == 0:
        return 0
    prev = list(range(-1, M - 1))
    nxt = list(range(1, M + 1))
    prev[0] = -1
    nxt[M - 1] = -1
    val = vals[:]
    ver = [0] * M
    heap = [(-val[i], i, 0) for i in range(M)]
    heapq.heapify(heap)
    ans = 0
    for _ in range(K):
        while heap:
            neg_v, i, v = heapq.heappop(heap)
            if ver[i] == v:
                break
        else:
            break
        v_val = -neg_v
        ans += v_val
        L = prev[i]
        R = nxt[i]
        if L != -1 and R != -1:
            new_val = val[L] + val[R] - v_val
            prev[i] = prev[L]
            nxt[i] = nxt[R]
            if prev[i] != -1:
                nxt[prev[i]] = i
            if nxt[i] != -1:
                prev[nxt[i]] = i
            ver[L] += 1
            ver[R] += 1
            val[i] = new_val
            ver[i] += 1
            heapq.heappush(heap, (-new_val, i, ver[i]))
        elif L != -1:
            if prev[L] != -1:
                nxt[prev[L]] = -1
            ver[L] += 1
            ver[i] += 1
        elif R != -1:
            if nxt[R] != -1:
                prev[nxt[R]] = -1
            ver[R] += 1
            ver[i] += 1
        else:
            ver[i] += 1
    return ans

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []
    for _ in range(T):
        N = int(data[idx]); idx += 1
        K = int(data[idx]); idx += 1
        cakes = []
        for i in range(N):
            x = int(data[idx]); idx += 1
            y = int(data[idx]); idx += 1
            z = int(data[idx]); idx += 1
            cakes.append((x, y, z))
        best = 0
        for dim in range(3):
            sorted_cakes = sorted(cakes, key=lambda c: -c[dim])
            M = N - 1
            vals = []
            for i in range(M):
                a = sorted_cakes[i]
                b = sorted_cakes[i + 1]
                vals.append(max(a[0] + b[0], a[1] + b[1], a[2] + b[2]))
            ans = select_k_nonadjacent(vals, K)
            if ans > best:
                best = ans
        out.append(str(best))
    sys.stdout.write('\n'.join(out) + '\n')

solve()
```

### TASKS
- [todo] Rewrite solution.py with the 3-sort-orders + select-K-non-adjacent-adjacent-pairs algorithm (max-heap with doubly-linked-list undo trick). Replace the broken greedy-dominant-attribute approach entirely.
- [todo] Verify the new solution passes both provided samples (expected outputs: 12, and 209+333).
- [todo] Run stress test (200 random small inputs vs brute force) to confirm correctness. Pay special attention to the previously-failing case (N=4,K=1 with cakes (17,15,7),(0,13,13),(9,13,19),(12,4,7) → answer must be 32).
- [todo] Performance check: single test case N=100000, K=50000 should run in well under 2 seconds in Python. Optimize constants if needed (local variable caching, avoid lambda in tight loops).
