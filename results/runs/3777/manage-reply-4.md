### STATUS
continue
### NEXT
Fix the bug where intermediate products exceeding `limit` are discarded even though a later 0 would make the final product 0. Restructure the DP into three state categories per (parity, alt_sum):

1. `dp_nozero[p][s]` = max product in [1, limit] achievable (no zero in subsequence), or -1.
2. `dp_over[p][s]` = boolean: achievable without any zero but product > limit (can only recover if a 0 comes later).
3. `dp_zero[p][s]` = boolean: achievable with at least one zero (product is 0).

Process each element x with a snapshot of all three tables (0/1 knapsack style). Transitions:

- **x > 0:**
  - Start: if x ≤ limit → dp_nozero[1][x] = max(..., x); else dp_over[1][x] = True.
  - From dp_nozero[p][s]: new_prod = prod * x. If new_prod ≤ limit → update dp_nozero[1-p][s±x]; else → dp_over[1-p][s±x] = True.
  - From dp_over[p][s]: product stays > limit → dp_over[1-p][s±x] = True.
  - From dp_zero[p][s]: product stays 0 → dp_zero[1-p][s±x] = True.

- **x == 0:**
  - Start: dp_zero[1][0] = True.
  - From dp_nozero[p][s]: product becomes 0 → dp_zero[1-p][s] = True.
  - From dp_over[p][s]: product becomes 0 → dp_zero[1-p][s] = True.
  - From dp_zero[p][s]: product stays 0 → dp_zero[1-p][s] = True.

Final answer: check dp_nozero[0][k], dp_nozero[1][k] for max product ≥ 1; check dp_zero[0][k] or dp_zero[1][k] for product 0. Return the max, or -1.

Use OFFSET = sum(nums), SIZE = 2*sum(nums)+1 for array indexing of alt_sum. Early-exit if abs(k) > sum(nums). Write the complete function with a return statement. Verify it passes the failing stress case: nums=[3,7,10,9,9,0], k=-4, limit=2 → answer must be 0 (subsequence [3,7,0]: alt_sum=3-7+0=-4, product=0).

### TASKS
- [done] Implement the DP table mapping (alt_sum, parity) → set of products, iterate elements with start/extend/skip.
- [done] Handle starting new subsequence, extending with parity flip, and skipping (implicit).
- [todo] Rewrite DP with three state categories (dp_nozero, dp_over, dp_zero) to handle the case where intermediate product > limit but a later 0 makes final product 0.
- [todo] Add final lookup: return max of dp_nozero[·][k] and dp_zero[·][k] (→0), or -1.
- [todo] Run against all 3 samples and the stress-failing input [3,7,10,9,9,0], k=-4, limit=2 (expected 0).
