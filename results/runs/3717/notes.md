- **Core decomposition:** (1) compute cost[i] = sum of |nums[j] - median| for each window of size x starting at i, (2) pick k non-overlapping windows via DP minimizing total cost.
- **Window cost via BIT + coordinate compression:** Compress all values to [1, comp_size]. Maintain two Fenwick trees (counts and sums). For each window, find the (x//2+1)-th smallest via BIT kth() in O(log n). Cost = median*count_below - sum_below + sum_above - median*count_above. Sliding: remove one, add one, recompute. Total O(n log n).
- **Why lower/upper median doesn't matter:** For even x, any value between the two middle elements gives the same sum of absolute deviations, so using the (x//2+1)-th smallest is always correct.
- **DP:** dp[i][j] = min cost to place j non-overlapping x-windows in first i positions. Recurrence: dp[i][j] = min(dp[i-1][j], dp[i-x][j-1] + cost[i-x]). Rolling arrays over j keep space O(n). Since all costs are non-negative, "at least k" = "exactly k".
- **Complexity:** O(n log n + n·k) time, O(n) space. For n=10^5, k=15: well within limits.
- **Verified both samples:** Example 1 → 8, Example 2 → 3.
- **Edge cases handled:** x=n (m=1, k must be 1 by constraint), all same values (cost=0), negative values (coordinate compression handles them), k=1.

