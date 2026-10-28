### STATUS
continue

### NEXT
Rewrite solution.py completely and cleanly (the previous attempt was truncated mid-DFS). The correct algorithm:
1. Build mapping f: for each char c in S, f[c] = corresponding char in T. If any c maps to two different values → print -1.
2. Count E = number of i where f[i] != -1 and f[i] != i (non-identity edges). If E == 0 → print 0.
3. Detect cycles in the directed graph on {0..25} with edges i→f[i] (only for f[i]!=-1). Count C = number of cycles. Track the maximum cycle length.
4. If max_cycle_length == 26 → print -1 (all 26 letters in one cycle, no temp available).
5. Otherwise → print E + C.

Write the complete code, save to solution.py, run it on all 4 samples, and then run the stress test (`python3 stress.py` or the equivalent) to confirm it passes 200 random inputs against brute.py. If brute.py itself is buggy/crashes, fix brute.py so the stress test can complete.

### TASKS
- [done] Build the per-character mapping from S to T; if inconsistent, output -1.
- [done] Count non-identity edges E; if E==0, output 0.
- [done] Identify impossibility: cycle of length 26 → -1.
- [todo] Rewrite solution.py completely (previous was truncated mid-DFS loop). Implement full cycle detection via iterative DFS with coloring, compute C and max_cycle_length, apply formula E+C or -1.
- [todo] Verify solution.py on all 4 samples and run 200-iteration stress test against brute.py; fix brute.py if it crashes.
