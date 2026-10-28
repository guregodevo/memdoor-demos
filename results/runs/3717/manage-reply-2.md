### STATUS
done
### NEXT
### TASKS
- [done] Implement sliding-window cost computation (sum of absolute deviations from median for each window of size x) using a BIT/Fenwick tree over compressed values.
- [done] Implement the DP to select k non-overlapping subarrays minimizing total cost: dp[i][j] = min(dp[i-1][j], dp[i-x][j-1] + cost[i-x]).
- [done] Write the final solution.py with Solution.minOperations wiring cost computation and DP together.
- [done] Edge-case and complexity check (k=1, x=n, negative values); brute-force cross-check on 200 small random inputs passed.
