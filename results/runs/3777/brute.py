from typing import List

class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n = len(nums)
        best = -1
        # Enumerate all 2^n - 1 non-empty subsequences by bitmask
        for mask in range(1, 1 << n):
            # Build the subsequence (maintaining original order)
            subseq = []
            for i in range(n):
                if mask & (1 << i):
                    subseq.append(nums[i])
            
            # Compute alternating sum: even indices subtracted from odd... 
            # Actually: sum at even indices - sum at odd indices
            alt_sum = 0
            for i in range(len(subseq)):
                if i % 2 == 0:
                    alt_sum += subseq[i]
                else:
                    alt_sum -= subseq[i]
            
            if alt_sum != k:
                continue
            
            # Compute product
            product = 1
            for x in subseq:
                product *= x
            
            if product <= limit and product > best:
                best = product
        
        return best
