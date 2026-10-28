### STATUS
continue

### NEXT
Implement the solution using the sorted-array formula: sort A, compute prefix sums, for even N answer = (PS[N] - PS[N//2]) - (PS[N//2] - PS[0]); for odd N (N=2m+1) compute C1 = (PS[N] - 2*PS[m+1]) + B[m-1], C2 = PS[N] - PS[m+1] - PS[m], C3 = (PS[N] - 2*PS[m]) - B[m+1], and return max(C1, C2, C3). Handle N=2 as a special case (answer = |A[0]-A[1]|). Write to solution.py and test against all 3 samples.

### TASKS
- [todo] Implement the sorting + prefix-sum solution (even and odd N formulas) in solution.py
- [todo] Test against all 3 provided samples and verify correctness
- [todo] Stress test against brute force for small N (N ≤ 8) to catch edge cases
