from typing import List

class BIT:
    __slots__ = ('size', 'tree')
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, idx, delta):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx)
    
    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s
    
    def kth(self, k):
        pos = 0
        bit_mask = 1 << (self.size.bit_length() - 1)
        while bit_mask:
            next_pos = pos + bit_mask
            if next_pos <= self.size and self.tree[next_pos] < k:
                pos = next_pos
                k -= self.tree[next_pos]
            bit_mask >>= 1
        return pos + 1

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        m = n - x + 1
        
        sorted_vals = sorted(set(nums))
        val_to_idx = {v: i + 1 for i, v in enumerate(sorted_vals)}
        comp_size = len(sorted_vals)
        
        count_bit = BIT(comp_size)
        sum_bit = BIT(comp_size)
        
        for i in range(x):
            idx = val_to_idx[nums[i]]
            count_bit.update(idx, 1)
            sum_bit.update(idx, nums[i])
        
        cost = [0] * m
        
        def compute_cost():
            median_idx = count_bit.kth(x // 2 + 1)
            median_val = sorted_vals[median_idx - 1]
            count_below = count_bit.query(median_idx - 1)
            sum_below = sum_bit.query(median_idx - 1)
            count_at = count_bit.query(median_idx) - count_below
            sum_at = sum_bit.query(median_idx) - sum_below
            count_above = x - count_below - count_at
            total_sum = sum_bit.query(comp_size)
            sum_above = total_sum - sum_below - sum_at
            return median_val * count_below - sum_below + sum_above - median_val * count_above
        
        cost[0] = compute_cost()
        
        for i in range(1, m):
            ri = val_to_idx[nums[i - 1]]
            count_bit.update(ri, -1)
            sum_bit.update(ri, -nums[i - 1])
            ai = val_to_idx[nums[i + x - 1]]
            count_bit.update(ai, 1)
            sum_bit.update(ai, nums[i + x - 1])
            cost[i] = compute_cost()
        
        INF = float('inf')
        prev = [0] * (n + 1)
        
        for j in range(1, k + 1):
            curr = [INF] * (n + 1)
            for i in range(1, n + 1):
                curr[i] = curr[i - 1]
                if i >= x:
                    v = prev[i - x] + cost[i - x]
                    if v < curr[i]:
                        curr[i] = v
            prev = curr
        
        return prev[n]
