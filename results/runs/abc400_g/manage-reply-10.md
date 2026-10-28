Looking at the stress failure, the solution gives 64 but the correct answer is 67. The optimal pairing is (cake2,cake4) with Y winning (price 34) and (cake3,cake6) with X winning (price 33), total 67. The "sort by one dimension and pair adjacent" approach is fundamentally flawed because the optimal matching can mix winning dimensions across pairs.

After careful analysis, I discovered the key insight: **the true optimal equals the "relaxed" 3-way assignment problem** (no validity constraint needed). The proof: (1) any true matching gives a valid relaxed solution of equal value (assign each pair's cakes to the winning dimension), so relaxed ≥ true. (2) any relaxed solution, when paired within groups, has true total ≥ relaxed total (since max ≥ chosen dim), so true ≥ relaxed. Therefore true = relaxed.

The relaxed problem is: select 2K cakes and assign each to X, Y, or Z (even count per dimension) to maximize total assigned value. This reduces to: select top 2K by max(X,Y,Z), assign each to its argmax dimension, and fix parity (at most 2 dimensions have odd count) with minimum cost.

### STATUS
continue

### NEXT
Rewrite solution.py from scratch using the correct algorithm:

**Key theorem:** The answer to the original problem equals the maximum, over all ways to select exactly 2K cakes and assign each to one of {X,Y,Z} with an even count per dimension, of the sum of the assigned coordinate values. (Proof: any K-matching maps to such an assignment with equal value; any such assignment maps to a K-matching with >= value. So the two optima are equal.)

**Algorithm per test case:**
1. For each cake i, compute m[i] = max(X[i], Y[i], Z[i]).
2. Sort cakes by m[i] descending. Let S = top 2K cakes. Compute total = sum of m[i] for i in S.
3. For each i in S, find best_dim[i] = argmax(X[i], Y[i], Z[i]) (tie-break: prefer the dimension that helps parity, or just pick first). Count cnt[X], cnt[Y], cnt[Z].
4. If all cnt are even: answer = total.
5. If exactly two dimensions (say a and b) have odd count (the third, c, is even):
   Compute the minimum "fix cost" among these options:
   - **Option A:** Reassign one cake from dim a to dim b (or vice versa). Cost = min( min_{i in S, best=a}(val_a[i]-val_b[i]), min_{i in S, best=b}(val_b[i]-val_a[i]) ). (If a cake has a tie in its best dim, the cost could be 0.)
   - **Option B:** Reassign one cake from dim a to dim c AND one from dim b to dim c. Cost = min_{i in S,best=a}(val_a[i]-val_c[i]) + min_{j in S,best=b}(val_b[j]-val_c[j]).
   - **Option C:** Unselect one cake from dim a (lose val_a[i]) and select one previously-unselected cake for dim b (gain val_b[j]). Net cost = val_a[i] - val_b[j]. Minimize over i in S with best=a, j not in S. Similarly for the reverse (unselect from b, select for a). Take the min of both directions. If N==2K (no unselected cakes), skip this option.
   - **Option D:** Unselect one from dim a and one from dim b, select two unselected cakes for dim c. Cost = min_{i in S,best=a}(val_a[i]) + min_{j in S,best=b}(val_b[j]) - (top1_val_c_unselected + top2_val_c_unselected). Only valid if at least 2 unselected cakes exist.
   
   Answer = total - min(fix costs from available options).

6. Print the answer.

**Implementation details:**
- Use sys.stdin.buffer for fast I/O.
- For each test case: read N, K, then N lines of (X,Y,Z).
- Sort indices by m[i] descending (O(N log N)).
- For parity fix, precompute: for each dimension d, the min of (val_d[i] - val_e[i]) over selected cakes with best_dim=d (for options A, B). Also precompute the top-2 unselected cakes by each dimension value (for options C, D).
- Handle ties in argmax carefully: if two dimensions tie for best, the cake can be assigned to either at zero cost. To handle this, when computing min costs for options A/B, also consider cakes whose best is tied (cost 0 to reassign to the tied dim).
- Edge cases: K=1 (only 2 cakes selected), N=2K (no unselected cakes, skip options C/D).

**Verification:** Must pass both samples AND the stress test case:
```
3
2 1
2 0 6
2 8 0
6 3
4 9 12
5 19 17
5 13 4
8 5 11
3 11 10
8 14 3
8 2
6 12 6
16 14 8
15 4 4
15 20 1
5 10 1
18 15 13
8 8 13
14 4 7
```
Expected output:
```
8
80
67
```

### TASKS
- [done] Implement fast input parsing for T test cases
- [done] Implement the core subroutine `select_k_nonadjacent` (abandoned - approach was wrong)
- [done] Implement the main solver with 3-sorting approach (WRONG - fails stress test)
- [todo] Rewrite solution.py with the correct 3-way-assignment + parity-fix algorithm as described in NEXT
- [todo] Run against both samples and the stress-failing input to verify correctness
- [todo] Stress test with 200+ random small inputs against brute force
