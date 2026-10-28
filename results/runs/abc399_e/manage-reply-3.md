### STATUS
continue

### NEXT
The stress test failed because brute.py crashed/timed out on input "7\nxzosssz\ndgsbzmf" (solution.py correctly output -1 since the S→T mapping is not well-defined: z maps to both g and f, o maps to both s and z, s maps to b, m, and f). Fix brute.py so that it FIRST checks whether the per-character mapping from S to T is a well-defined function (i.e., every character appearing in S maps to exactly one character in T). If it is not, immediately print -1 and exit without attempting any BFS or search. Only if the mapping IS well-defined should brute.py attempt its search. Rewrite /Users/gregoryd/memdoor-coder/lcb-bench/brute.py with this guard at the top. After fixing, re-run the stress test: `python3 /Users/gregoryd/memdoor-coder/lcb-bench/grade.py --public abc399_e --stress` to confirm all 200 iterations pass.

### TASKS
- [done] Build the per-character mapping from S to T; if any character in S maps to two different characters in T, immediately output -1.
- [done] Construct the functional graph on the 26 lowercase letters using only edges where f(c) ≠ c; identify all cycles (via visited-state traversal) and count total edges |E| and number of cycles C.
- [done] Handle the impossibility case: if any detected cycle has length 26, output -1; otherwise output |E| + C.
- [done] Implement the complete solution in `solution.py` reading N, S, T from stdin and printing the answer to stdout.
- [done] Run `python3 solution.py` against all four provided samples to verify correctness — all 4 PASS.
- [todo] Fix brute.py: add an early-exit check for ill-defined S→T mapping (print -1) before any expensive search, then re-run the full 200-iteration stress test to confirm no crashes and solution matches brute on all cases.
