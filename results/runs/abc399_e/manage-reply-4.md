### STATUS
continue

### NEXT
Replace the entire solution.py with the correct graph-based algorithm. The BFS-over-string-states approach is infeasible (state space 26^N). Implement instead:

1. Read N, S, T.
2. Build mapping `f`: for each position i, f[S[i]] must equal T[i]. If any character in S maps to two different characters in T, print -1 and return.
3. If S == T, print 0 and return.
4. Build a directed graph on 26 nodes (a–z) with an edge c → f(c) ONLY when f(c) ≠ c. (Characters that don't appear in S have no outgoing edge.)
5. Detect all cycles in this functional graph (each node has out-degree ≤ 1, so cycles are disjoint). Count:
   - `E` = number of non-trivial edges (where f(c) ≠ c)
   - `C` = number of distinct cycles
6. If any cycle has length exactly 26 (all 26 letters in one cycle), print -1 (no free temporary letter exists).
7. Otherwise print `E + C`.

Write clean, complete Python code in solution.py. Verify against all 4 samples.

### TASKS
- [done] Build the per-character mapping from S to T; if any character in S maps to two different characters in T, immediately output -1.
- [todo] Implement the full graph-based solution: build 26-node functional graph (edges c→f(c) where f(c)≠c), detect cycles, compute answer as E + C, handle the 26-cycle impossibility case, write to solution.py, and verify all 4 samples.
- [todo] Run stress test (200 random small inputs vs brute-force) to confirm correctness.
