### STATUS
continue
### NEXT
Write the complete solution.py implementing the full algorithm: (1) fast input parsing for T test cases; (2) the core subroutine select_k_nonadjacent(vals, K) using a max-heap with doubly-linked-list and the undo-element trick (pop max, remove it and its two neighbors, push a virtual node with value left+right-center; handle boundaries where a neighbor is missing); (3) the main per-case solver that tries three sort orders (by X desc, by Y desc, by Z desc), for each computes the N-1 adjacent-pair values as max(X_i+X_{i+1}, Y_i+Y_{i+1}, Z_i+Z_{i+1}), calls select_k_nonadjacent, and takes the max over the three; (4) I/O wrapper printing one answer per line. Use sys.stdin for fast reading. After writing, run it against both samples to verify output matches exactly.
### TASKS
- [todo] Write complete solution.py (input parsing, select_k_nonadjacent with heap+linked-list undo, three-sort-order main solver, I/O) and verify against both samples
- [todo] Run timing check on worst-case input (N=100000, K=50000); optimize constants if too slow
- [todo] Stress-test against brute force on small random inputs to catch edge cases
