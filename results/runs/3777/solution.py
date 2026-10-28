from typing import List

class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        total = sum(nums)
        if abs(k) > total:
            return -1
        
        # dp_nozero[p] = dict: s -> set of products in [1, limit] (no zeros in subsequence)
        # dp_over[p] = set of s values (product > limit, no zeros yet)
        # dp_zero[p] = set of s values (product = 0, at least one zero in subsequence)
        # p=0: next element gets + sign; p=1: next element gets - sign
        
        dp_nozero = [dict(), dict()]
        dp_over = [set(), set()]
        dp_zero = [set(), set()]
        
        for x in nums:
            # Snapshot for 0/1 knapsack (avoid reusing current element)
            snap_nozero = [dict() for _ in range(2)]
            for p in range(2):
                for s, prods in dp_nozero[p].items():
                    snap_nozero[p][s] = frozenset(prods)
            snap_over = [set(dp_over[p]) for p in range(2)]
            snap_zero = [set(dp_zero[p]) for p in range(2)]
            
            if x > 0:
                # Start new subsequence with x (x at index 0, +sign, next parity=1)
                if x <= limit:
                    dp_nozero[1].setdefault(x, set()).add(x)
                else:
                    dp_over[1].add(x)
                
                # Extend existing subsequences
                for p in range(2):
                    sign = 1 if p == 0 else -1
                    np = 1 - p
                    
                    # From dp_nozero
                    for s, prods in snap_nozero[p].items():
                        new_s = s + sign * x
                        if abs(new_s) > total:
                            continue
                        for prod in prods:
                            new_prod = prod * x
                            if new_prod <= limit:
                                dp_nozero[np].setdefault(new_s, set()).add(new_prod)
                            else:
                                dp_over[np].add(new_s)
                    
                    # From dp_over (product stays > limit)
                    for s in snap_over[p]:
                        new_s = s + sign * x
                        if abs(new_s) <= total:
                            dp_over[np].add(new_s)
                    
                    # From dp_zero (product stays 0)
                    for s in snap_zero[p]:
                        new_s = s + sign * x
                        if abs(new_s) <= total:
                            dp_zero[np].add(new_s)
            
            else:  # x == 0
                # Start new subsequence [0]: alt_sum=0, product=0, next parity=1
                dp_zero[1].add(0)
                
                # Extend existing (alt_sum unchanged since x=0)
                for p in range(2):
                    np = 1 - p
                    
                    # From dp_nozero: product becomes 0
                    for s in snap_nozero[p]:
                        dp_zero[np].add(s)
                    
                    # From dp_over: product becomes 0
                    for s in snap_over[p]:
                        dp_zero[np].add(s)
                    
                    # From dp_zero: product stays 0
                    for s in snap_zero[p]:
                        dp_zero[np].add(s)
        
        # Final answer: look up k in both parities
        best = -1
        for p in range(2):
            if k in dp_nozero[p]:
                best = max(best, max(dp_nozero[p][k]))
        
        for p in range(2):
            if k in dp_zero[p]:
                best = max(best, 0)
        
        return best
