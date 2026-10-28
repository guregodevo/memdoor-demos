### PLAN
The key insight is that the maximum total score equals (sum of the largest ⌊N/2⌋ values) minus (sum of the smallest ⌊N/2⌋ values) when N is even, and the max of 3 specific candidates when N is odd. This works because: (1) any pairing that matches each "small-half" element with a "large-half" element yields the same total regardless of which specific pairs are formed, and (2) a non-crossing matching with this property always exists (proven via a stack-based greedy argument on the color-coded sequence). The algorithm is therefore: sort the array, then compute the answer in O(1) using prefix sums. For odd N, only 3 candidates (removing the (m-1)-th, m-th, or (m+1)-th smallest element) need to be checked.

### TASKS
- **Implement the sorting and prefix-sum computation**: Read N and the array A, sort it into B, and compute prefix sums PS[0..N].
- **Implement the even-N formula**: If N is even, compute answer = sum(B[N/2:]) - sum(B[:N/2]) using the prefix sums (PS[N] - PS[N/2] - (PS[N/2] - PS[0])).
- **Implement the odd-N formula**: If N is odd (N=2m+1), compute three candidates using the derived closed forms: C1 = (PS[2m+1] - 2*PS[m+1]) + B[m-1], C2 = PS[2m+1] - PS[m+1] - PS[m], C3 = (PS[2m+1] - 2*PS[m]) - B[m+1], and return max(C1, C2, C3).
- **Handle I/O and edge cases**: Ensure correct reading from stdin and writing to stdout; verify N=2 works (reduces to |A[0]-A[1]|) and all-equal arrays return 0.
- **Test against all 3 provided samples** and a few additional small cases (brute-force verify for N ≤ 8 by enumerating all non-crossing matchings) to confirm correctness before submitting.
