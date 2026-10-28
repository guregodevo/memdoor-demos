Looking at the stress test failure, the solution output 98 but the correct answer is 103 for the second test case (N=7, K=3).

Let me analyze the problem structure. The key insight I missed: `max(X_i+X_j, Y_i+Y_j, Z_i+Z_j)` for a pair can be decomposed using each item's "dominant dimension" (the dimension where it has its max value). When two items share the same dominant dimension, their pair value equals the sum of their individual max values (zero "waste"). When they differ, there's a "waste" equal to `min(gap_i, gap_j)` where gaps are how much the dominant dimension exceeds the partner's dominant dimension.

The answer = (sum of top 2K individual max values) − (waste from at most one cross-dimension pair, determined by group parities).

This completely replaces the flawed "sort by one dimension, pick adjacent pairs" approach.

### STATUS
continue

### NEXT
Replace the entire solution with a new approach based on the "dominant dimension + waste" framework:

1. For each item, compute S_i = max(X_i, Y_i, Z_i) and its dominant dimension (tie-break X > Y > Z).
2. Sort all items by S_i descending. Select the top 2K items.
3. Group selected items by dominant dimension into groups g0 (X), g1 (Y), g2 (Z). For each item in group d, store its gaps to the other two dimensions (e.g., X-dominant item stores (X-Y, X-Z)).
4. Compute total_max = sum of S_i over selected items.
5. Determine which groups have odd size. Since 2K is even, either 0 or 2 groups are odd.
   - If 0 odd groups: waste = 0.
   - If 2 odd groups (say a and b): waste = min(min_gap_in_group_a_to_b, min_gap_in_group_b_to_a).
6. Answer = total_max - waste.

Gap references:
- Group 0 (X-dom) stores (x-y, x-z). Gap to Y = index 0, gap to Z = index 1.
- Group 1 (Y-dom) stores (y-x, y-z). Gap to X = index 0, gap to Z = index 1.
- Group 2 (Z-dom) stores (z-x, z-y). Gap to X = index 0, gap to Y = index 1.

Waste formulas:
- X-odd + Y-odd: min(min(v[0] for v in g0), min(v[0] for v in g1))
- X-odd + Z-odd: min(min(v[1] for v in g0), min(v[0] for v in g2))
- Y-odd + Z-odd: min(min(v[1] for v in g1), min(v[1] for v in g2))

The full solution.py should be:
```python
import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []
    for _ in range(T):
        N = int(data[idx]); idx += 1
        K = int(data[idx]); idx += 1
        items = []
        for i in range(N):
            x = int(data[idx]); idx += 1
            y = int(data[idx]); idx += 1
            z = int(data[idx]); idx += 1
            items.append((x, y, z))
        scored = [(max(x,y,z), x, y, z) for x,y,z in items]
        scored.sort(key=lambda t: -t[0])
        sel = scored[:2*K]
        total_max = sum(t[0] for t in sel)
        g0, g1, g2 = [], [], []
        for mx, x, y, z in sel:
            if x >= y and x >= z:
                g0.append((x-y, x-z))
            elif y >= x and y >= z:
                g1.append((y-x, y-z))
            else:
                g2.append((z-x, z-y))
        n0, n1, n2 = len(g0), len(g1), len(g2)
        odds = [i for i, n in enumerate([n0,n1,n2]) if n & 1]
        if not odds:
            waste = 0
        else:
            a, b = odds
            if a == 0 and b == 1:
                waste = min(min(v[0] for v in g0), min(v[0] for v in g1))
            elif a == 0 and b == 2:
                waste = min(min(v[1] for v in g0), min(v[0] for v in g2))
            else:
                waste = min(min(v[1] for v in g1), min(v[1] for v in g2))
        out.append(str(total_max - waste))
    sys.stdout.write('\n'.join(out) + '\n')

solve()
```

Verify against both samples before submitting. This should handle the stress failing case (second test: top 6 items give groups X:2, Y:3, Z:1 → odd Y,Z → waste=min(0,2)=0 → answer=103).

### TASKS
- [done] Implement fast input parsing for T test cases
- [done] Implement the "sort by dominant dimension, select K non-adjacent" approach (ABANDONED - incorrect)
- [todo] Implement the new "dominant dimension + waste" solution (code provided above)
- [todo] Run against both samples and the stress-failing input to verify
- [todo] Stress test against brute force (200 random inputs)
