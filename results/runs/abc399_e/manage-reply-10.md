### STATUS
continue

### NEXT
Review and finalize `solution.py` end-to-end. The code display was truncated at the cycle-detection loop, so confirm the file on disk is syntactically complete. Most importantly, verify the impossibility condition is correct: the answer is -1 **only** when (a) at least one cycle exists in the non-identity functional graph, (b) all 26 letters appear in S (no free letter), AND (c) every letter that appears in S is part of a cycle (i.e., there are zero tree/non-cycle nodes among the 26). If any of (a)-(c) fails, the answer is E + C (non-identity edges + number of cycles). For the stress input `N=7, S=sbmbkio, T=oassmsm`, the mapping is inconsistent (b→a at pos 1, b→s at pos 3), so -1 is correct; the stress failure was brute.py crashing, not the solution. After confirming/fixing the code, re-run all 4 samples and then generate 50 targeted random tests (small N, biased toward all-26-letter S and cycles) comparing against a correct brute-force that tries all sequences of ≤6 renames via BFS/DFS.

### TASKS
- [done] Build the per-character mapping from S to T; if any character in S maps to two different characters in T, immediately output -1.
- [done] Construct the functional graph on the 26 lowercase letters using only edges where f(c) ≠ c; identify all cycles and count total edges |E| and number of cycles C.
- [todo] Verify and finalize the impossibility condition in `solution.py`: answer is -1 iff (cycle exists) AND (all 26 letters in S) AND (all 26 letters are in cycles, no tree nodes). Otherwise answer is |E| + C. Ensure the code is syntactically complete and handles this correctly.
- [todo] Re-run all 4 samples, then run 50 targeted random tests (N up to 8, biased toward S using all/most of 26 letters and containing cycles) against a correct brute-force reference to confirm no off-by-one or missing-edge bugs.
