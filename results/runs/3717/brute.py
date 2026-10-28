from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        # Compute the cost to make each window of size x all equal
        # (optimal target is the median, minimizing sum of absolute diffs)
        costs = []
        for i in range(n - x + 1):
            window = nums[i:i + x]
            window_sorted = sorted(window)
            median = window_sorted[x // 2]
            cost = sum(abs(v - median) for v in window)
            costs.append(cost)
        
        INF = float('inf')
        
        # Brute-force DFS: pick k non-overlapping windows of size x
        # A window starting at position i occupies indices [i, i+x-1]
        # So the next window must start at >= i + x
        def dfs(start, remaining):
            if remaining == 0:
                return 0
            if start >= len(costs):
                return INF
            best = INF
            for i in range(start, len(costs)):
                # Choose window starting at position i
                rest = dfs(i + x, remaining - 1)
                if rest < INF:
                    candidate = costs[i] + rest
                    if candidate < best:
                        best = candidate
            return best
        
        result = dfs(0, k)
        return result
