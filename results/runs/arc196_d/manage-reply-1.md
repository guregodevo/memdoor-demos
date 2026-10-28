Looking at this problem, I need to:
1. Characterize when a set of people is infeasible (conflicting pairs)
2. Compute `prev[j]` = max index i < j that conflicts with j
3. Answer queries using range-max on prev[]

The conflict conditions are:
- **Same direction**: intervals properly cross (a_i < a_j < b_i < b_j or symmetric)
- **Opposite direction**: share a same-side endpoint (a_i = a_j or b_i = b_j)

I'll use CDQ divide-and-conquer for crossing detection and a sparse table for query answering.

Let me verify my analysis against both samples manually, then write the solution.

### STATUS
continue

### NEXT
Write solution.py implementing the full approach: (1) compute prev[j] via endpoint-conflict scan + CDQ for same-direction crossings, (2) build sparse table over prev[], (3) answer each query (L,R) by checking if max(prev[L+1..R]) >= L. Use fast I/O (sys.stdin.buffer), iterative segment tree, and local variable optimization in the CDQ inner loops. Test on both samples.

### TASKS
- [todo] Write solution.py: full implementation (endpoint conflicts + CDQ crossing detection + sparse table queries)
- [todo] Test on both provided samples, verify correct output
- [todo] If samples pass, run stress test against brute force on small random inputs
- [todo] If performance is too slow, optimize CDQ (merge-sort style, reduce Python overhead) or switch approach
