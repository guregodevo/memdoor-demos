from typing import List


class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        # Precompute prefix sums
        nums_prefix = [0] * n
        nums_prefix[0] = nums[0]
        for i in range(1, n):
            nums_prefix[i] = nums_prefix[i - 1] + nums[i]

        cost_prefix = [0] * n
        cost_prefix[0] = cost[0]
        for i in range(1, n):
            cost_prefix[i] = cost_prefix[i - 1] + cost[i]

        best = float('inf')

        # Brute force: enumerate all 2^(n-1) ways to place cuts
        for mask in range(1 << (n - 1)):
            total_cost = 0
            subarray_idx = 1  # 1-indexed order of subarray
            start = 0
            for i in range(n - 1):
                if mask & (1 << i):
                    # Subarray is [start..i]
                    if start == 0:
                        c_sum = cost_prefix[i]
                    else:
                        c_sum = cost_prefix[i] - cost_prefix[start - 1]
                    total_cost += (nums_prefix[i] + k * subarray_idx) * c_sum
                    subarray_idx += 1
                    start = i + 1

            # Last subarray: [start..n-1]
            if start == 0:
                c_sum = cost_prefix[n - 1]
            else:
                c_sum = cost_prefix[n - 1] - cost_prefix[start - 1]
            total_cost += (nums_prefix[n - 1] + k * subarray_idx) * c_sum

            if total_cost < best:
                best = total_cost

        return best
