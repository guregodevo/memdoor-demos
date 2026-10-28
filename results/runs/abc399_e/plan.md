### PLAN
The problem reduces to analyzing a functional graph over at most 26 lowercase letters where each character c in S maps to f(c) in T. First, verify the mapping is consistent (each S-character maps to exactly one T-character); if not, answer is -1. Next, build the directed graph of non-trivial mappings (edges where f(c)≠c); since each node has out-degree ≤ 1, the graph decomposes into chains and cycles. The minimum operations equal the number of non-trivial edges plus the number of cycles (each cycle of length k needs k+1 operations via a temporary letter). The only edge case making it impossible is a cycle of length 26 (all letters), where no free temporary exists.

### TASKS
- Build the per-character mapping from S to T; if any character in S maps to two different characters in T, immediately output -1.
- Construct the functional graph on the 26 lowercase letters using only edges where f(c) ≠ c; identify all cycles (via visited-state traversal) and count total edges |E| and number of cycles C.
- Handle the impossibility case: if any detected cycle has length 26, output -1; otherwise output |E| + C.
- Implement the complete solution in `solution.py` reading N, S, T from stdin and printing the answer to stdout.
- Run `python3 solution.py` against all four provided samples to verify correctness, then run the grader script.
