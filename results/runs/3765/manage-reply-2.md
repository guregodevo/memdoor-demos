### STATUS
done

### NEXT

### TASKS
- [done] Compute prefix sums `P[i]` and `C[i]`; set up the 2-D DP with base case `dp[i][1] = (P[i] + k) * C[i]`.
- [done] Implement a monotone-convex-hull (deque) CHT with `add_line` and `query` using cross-product comparisons (no floating point).
- [done] For each layer m = 2..n, iterate i from m to n: insert line for j=i-1, query at x = P[i]+k*m to get dp_curr[i].
- [done] Track running minimum over all m; handle n=1 edge case.
- [done] Verified against both samples (110, 985) and 200 random stress inputs vs brute force — all passed.
