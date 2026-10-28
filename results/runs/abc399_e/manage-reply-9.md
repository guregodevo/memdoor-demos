### STATUS
continue

### NEXT
Verify that solution.py on disk is syntactically complete (the previous report said it was truncated mid-DFS-loop at `if color[start] != 0:`). If it IS truncated, finish the code: the DFS body should walk `v = f[v]` while `color[v]==1`, mark `color[v]==2` when done, count a cycle when we hit a node already marked 1 (and its cycle length is 26 → print -1). After the loop, compute `ans = E + C` (if a free letter exists, still `E + C`; if NO free letter and C>0, print -1; if no free letter and C==0, print E). Print ans. Then re-run all 4 samples and re-run the 200-input stress test. Note: the previous stress "failure" was brute.py timing out on N=5 (26^5 state space), NOT solution.py giving a wrong answer (it correctly printed 5). If solution.py is already complete and correct on disk, simply re-run the grader and stress to confirm.

### TASKS
- [done] Build the per-character mapping from S to T; if any character in S maps to two different characters in T, immediately output -1.
- [done] Construct the functional graph on the 26 lowercase letters using only edges where f(c) ≠ c; identify all cycles (via visited-state traversal) and count total edges |E| and number of cycles C.
- [todo] Ensure solution.py is syntactically complete on disk: DFS cycle-count body, impossibility check (cycle of length 26 with no free letter → -1), final formula (ans = E + C if free letter exists; if no free letter and C > 0 → -1; if no free letter and C == 0 → E), and print. Re-run samples + stress.
- [done] Implement the complete solution in `solution.py` reading N, S, T from stdin and printing the answer to stdout.
- [done] Run `python3 solution.py` against all four provided samples to verify correctness (all 4 PASSED).
