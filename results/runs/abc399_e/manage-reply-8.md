### STATUS
continue

### NEXT
The stress test failed because brute.py crashed/timed out on iteration 4 (input: N=6, S=phupiv, T=cprqkd), while solution.py correctly output -1 (p maps to both c and q — inconsistent). The solution itself is correct on this input. Your job: (1) Fix or rewrite brute.py so it does NOT time out on small inputs (N≤8, random strings) — use a BFS/DFS over the state space of the 26-letter mapping with a proper operation-count lower bound to prune, or simply enumerate operation sequences up to length 6 for N≤8. Make sure it handles the inconsistent-mapping case (immediate -1) and the all-26-cycle case (immediate -1) without exponential blowup. (2) Re-run the stress comparison (200 random inputs, N≤8) between solution.py and the fixed brute.py. (3) If any mismatch is found, fix solution.py. Report the final stress verdict.

### TASKS
- [done] Build the per-character mapping from S to T; if any character in S maps to two different characters in T, immediately output -1.
- [done] Construct the functional graph on the 26 lowercase letters using only edges where f(c) ≠ c; identify all cycles (via visited-state traversal) and count total edges |E| and number of cycles C.
- [done] Handle the impossibility case: if any detected cycle has length 26, output -1; otherwise output |E| + C.
- [done] Implement the complete solution in `solution.py` reading N, S, T from stdin and printing the answer to stdout.
- [done] Run `python3 solution.py` against all four provided samples to verify correctness.
- [todo] Fix/rewrite brute.py for stress testing (N≤8) so it terminates quickly; re-run 200-input stress comparison; fix solution.py if any mismatch is found.
