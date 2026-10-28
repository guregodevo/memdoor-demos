### STATUS
continue

### NEXT
Fix the bug where the DP loses track of reachable states whose product exceeds `limit`. The failing case is `nums=[12,8,0,1,1], k=3, limit=23`: the subsequence [12,8,0,1] has alternating sum 3 and product 0, but the DP rejects the intermediate state (s=4,p=0,prod=96>23) and thus never reaches (s=3,p=0,prod=0).

**Root cause:** When a transition produces `new_prod = prod * x > limit`, the code discards the state entirely. But if a future element is 0, the product would reset to 0 (≤ limit). The DP must remember that the state is *reachable* even when no product ≤ limit is currently stored.

**Fix:** Add a boolean `reach[2][size]` array alongside `dp[2][size]`. A state `(s,p)` is reachable if any subsequence can achieve it (regardless of product). When processing element `x`:
- For every reachable state in the snapshot, compute the transition (new_s, new_p). Mark `reach[new_p][new_s+offset]=True`.
- If `x == 0`: set `dp[new_p][new_s+offset] = max(dp[new_p][new_s+offset], 0)` unconditionally (product resets to 0).
- If `x > 0` and `old_dp[p][s_idx] >= 0`: compute `new_prod = old_dp[p][s_idx] * x`; if `new_prod <= limit`, update dp. (If old_dp is -1, the product is >limit and any further non-zero multiply stays >limit, so skip.)
- "Start new subsequence" also sets both reach and dp.

At the end, answer = `max(dp[0][k+offset], dp[1][k+offset])` if ≥ 0, else -1.

Rewrite the full `solution.py` with this two-array approach. Keep the offset=1800, the snapshot-per-element logic, and the early exit `abs(k) > sum(nums) → -1`.

### TASKS
- [done] Implement the DP table mapping (alt_sum, parity) → max product, with offset 1800.
- [done] For each element: snapshot DP, compute take transition, handle start-new-subsequence, skip is implicit.
- [done] Final answer extraction: max(dp[0][k+offset], dp[1][k+offset]) or -1.
- [done] Handle edge cases: x=0, k=0, all-zero, limit=1, early exit.
- [done] Test against three provided samples (all pass).
- [todo] **Fix reachability bug:** add `reach[2][size]` boolean array so states with product > limit are not forgotten; when x=0, transition from any reachable state yields product 0. Rewrite solution.py with this fix.
- [todo] Re-run samples and stress (200 random inputs vs brute) to confirm fix.
