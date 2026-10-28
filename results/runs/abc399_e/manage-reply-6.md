### STATUS
continue

### NEXT
Rewrite `solution.py` from scratch with the complete, correct algorithm for the "Replace" problem. The algorithm is:

1. Read N, S, T. Build per-letter mapping f (size 26, init -1). For each position i, if S[i]=c and T[i]=d: if f[c] is -1 set it to d; elif f[c] != d, print -1 and return.
2. Count E = number of letters c where f[c] != -1 and f[c] != c. If E == 0, print 0 and return.
3. Build the directed graph on 26 nodes using only edges c -> f[c] where f[c] != -1 and f[c] != c. Detect cycles via standard DFS with 3-color marking (white/gray/black). Count C = number of cycles found. Also detect if any cycle includes all 26 non-identity nodes (not needed separately—see step 4).
4. Determine if a "free letter" exists: a letter c where f[c] == -1 (i.e., c never appears in S). Call this `has_free`.
5. If has_free: print E + C.
   Else (all 26 letters appear in S):
     - If C == 0: print E.
     - Else (C > 0, no free letter to break cycles): print -1.

Key insight: a cycle of length k requires k+1 operations (use a free letter as temporary). Without any free letter (all 26 in S), cycles cannot be broken → impossible. Identity letters (f[c]==c) in S are NOT free letters—they cannot serve as temporaries because they must remain unchanged in the output.

After writing, run all 4 samples to verify, then run a quick stress test against a brute-force checker on 50 small random inputs (N up to 8, alphabet up to 5 letters) to confirm correctness.

### TASKS
- [done] Build the per-character mapping from S to T; if any character in S maps to two different characters in T, immediately output -1.
- [done] Construct the functional graph on the 26 lowercase letters using only edges where f(c) ≠ c; identify all cycles (via visited-state traversal) and count total edges |E| and number of cycles C.
- [done] Handle the impossibility case: if no free letter exists (all 26 letters in S) and C > 0, output -1.
- [todo] Rewrite solution.py cleanly and completely implementing the full algorithm (mapping check → count E and C → check free letter → output E+C or -1 or E), ensuring no truncation.
- [todo] Verify the rewritten solution passes all 4 provided samples and a 50-input stress test on small alphabets.
