### STATUS
continue

### NEXT
Write `solution.py` that implements the full approach in one file: (1) Sieve all primes up to 10^6. (2) Precompute the sorted, deduplicated list of all 400 numbers ≤ 10^12 by iterating over every unordered pair of distinct primes (p < q); for each pair, loop a from 1 upward while p^(2a) * q^2 ≤ 10^12, and for each a loop b from 1 upward while p^(2a) * q^(2b) ≤ 10^12, collecting p^(2a) * q^(2b). Break early when the product exceeds 10^12. Sort and deduplicate. (3) Read Q and the Q values of A from stdin; for each A, use bisect_right on the precomputed list to find the largest 400 number ≤ A and print it. Use sys.stdin for fast I/O. Ensure the generation loops are tight (skip pairs where p^2 * q^2 > 10^12 immediately).

### TASKS
- [todo] Write complete `solution.py`: sieve primes ≤ 10^6, enumerate all 400 numbers ≤ 10^12 via (p<q, a≥1, b≥1) loops with early breaks, sort+dedup, answer Q queries via bisect_right. Use sys.stdin/sys.stdout.
- [todo] Run solution.py on sample input (5 queries: 404, 36, 60, 10^12, 123456789) and verify output is 400, 36, 36, 1000000000000, 123454321.
- [todo] Performance check: time a full run with Q=200000 random queries up to 10^12; confirm total runtime (precompute + queries) is under ~5 seconds in Python.
- [todo] Edge-case verification: A=36 gives 36, A=10^12 gives 10^12, smallest possible 400 number is 36=2²·3².
