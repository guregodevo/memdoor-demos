### STATUS
continue

### NEXT
Implement the full solution in solution.py using the DP approach described in the plan. Use a dictionary-based DP mapping (alt_sum_offset, parity) -> max_product (initially -1 for unreachable). Offset alt_sum by 1800 to use array indexing. For each element x in nums: (1) snapshot the current DP as a list of (state, product) pairs, (2) for each reachable (s, p, prod) in the snapshot, compute the "take" transition: if p==0 then new_s=s+x, new_p=1; if p==1 then new_s=s-x, new_p=0; new_prod=prod*x; if new_prod<=limit and new_s is within [-1800,1800], update dp[(new_s+offset, new_p)] = max(current, new_prod), (3) also handle "start new subsequence with x": state (x+offset, 1) with product x (if x<=limit), (4) skip is implicit since we only update, never remove. After all elements, answer = max(dp.get((k+offset,0),-1), dp.get((k+offset,1),-1)); return it if >=0, else -1. Write the complete solution.py file.

### TASKS
- [todo] Implement the DP solution in solution.py (dictionary/array based, alt_sum offset 1800, parity tracking, 0/1 style with snapshot)
- [todo] Test against all three provided samples and verify correct output
- [todo] Handle edge cases: x=0 (product becomes 0), k=0, all-zero array, limit=1, |k| > sum(nums) early exit, single-element arrays
