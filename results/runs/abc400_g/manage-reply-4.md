### STATUS
continue
### NEXT
Replace the current incorrect "sort by one attribute + select non-adjacent pairs" approach with a correct bitmask DP for maximum weight matching. For each test case: (1) precompute w[i][j] = max(X[i]+X[j], Y[i]+Y[j], Z[i]+Z[j]) for all pairs, (2) compute dp[mask] = max weight perfect matching on the subset of items indicated by mask (transition: pick lowest set bit i, try pairing with each other set bit j, dp[mask] = max_j (w[i][j] + dp[mask ^ (1<<i) ^ (1<<j)])), (3) answer = max dp[mask] over all masks with exactly 2K bits set. This is O(N * 2^N) per test case which is fine for the stress test (N <= ~12). Write the full solution.py with proper I/O parsing for T test cases. Do NOT use the greedy approach (it is provably incorrect — verified on the failing stress input where greedy gives 109 but correct answer is 114).
### TASKS
- [done] Implement fast input parsing for T test cases
- [done] Implement the core subroutine select_k_nonadjacent (REJECTED: approach is fundamentally incorrect)
- [todo] Replace with correct bitmask DP for max-weight K-matching: dp[mask] over 2^N states, transition on lowest set bit, answer = max over masks of size 2K
- [todo] Verify against both provided samples AND the stress-failing input (6 3 / 8 6 20 / 12 15 18 / 18 5 7 / 9 19 3 / 13 20 20 / 19 20 0 must output 114)
- [todo] Design and implement efficient O(N log N) algorithm for large N (up to 10^5) — the bitmask DP only works for N <= ~20; need a different approach (possibly: exploit that best pair is among {top-2-X, top-2-Y, top-2-Z} candidates with a more careful non-greedy selection, or a reduction to min-cost flow on a sparse graph, or a parametric/convex optimization approach)
