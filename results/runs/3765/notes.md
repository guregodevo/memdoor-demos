- **Problem structure:** Partition nums[0..n-1] into m contiguous subarrays. Cost of i-th subarray nums[l..r] is (P[r]+k*i)*(C[r]-C[l-1]) where P,C are prefix sums.
- **DP formulation:** dp[m][i] = min cost to partition first i elements into m subarrays. Base: dp[1][i]=(P[i]+k)*C[i]. Transition expands to dp[m][i] = (P[i]+k*m)*C[i] + min_j {(-C[j])*x + dp[m-1][j]} where x=P[i]+k*m.
- **CHT applicability:** Lines have slopes -C[j] (strictly decreasing as j grows since cost[i]>=1) and queries x=P[i]+k*m (strictly increasing since nums[i]>=1). Perfect for monotone deque CHT.
- **Redundancy check:** For lines A,B,C with m_A>m_B>m_C, B is redundant if (b_C-b_A)*(m_A-m_B) <= (b_B-b_A)*(m_A-m_C). Verified with hand examples.
- **Query pop:** Front line worse than next when (m_A-m_B)*x > b_B-b_A. Use strict > to handle ties safely.
- **Complexity:** O(n^2) total (n layers, O(n) per layer with amortized O(1) CHT ops). Values up to ~10^15, Python big ints handle fine.
- **Edge case n=1:** Return (nums[0]+k)*cost[0] directly.
- **Verified:** Example 1 gives 110, Example 2 expected 985 (traced logic matches).

