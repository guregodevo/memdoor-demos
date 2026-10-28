- **Core bug fixed:** The original single-table DP discarded intermediate products exceeding `limit`, losing the path where a later 0 would reduce the product to 0. Example: [3,7,0] with limit=2 gives product 21→0, but 21>2 was discarded.
- **Three-state DP:** Split into `dp_nozero[p][s]` (set of products in [1,limit]), `dp_over[p][s]` (bool: product>limit, no zeros yet), `dp_zero[p][s]` (bool: product=0). This correctly handles the "over-limit then zero" recovery.
- **Why sets of products (not just max):** A larger product P2 may exceed limit when multiplied by x, while a smaller P1 doesn't. Example: limit=10, products {3,5}, x=6: 3*6=18>10 but... wait, actually 5*6=30>10 too. But with limit=20: 5*6=30>20 but 3*6=18≤20. So we MUST keep all products, not just the max.
- **Parity convention:** p=0 means next element gets + sign, p=1 means next gets - sign. Starting with x puts it at index 0 (+), so next parity=1.
- **Bounds:** alt_sum ∈ [-total, total] where total=sum(nums)≤1800. Early exit if |k|>total.
- **Complexity:** For each element, iterate over all reachable states. In practice the sets are small (products bounded by limit≤5000, formed from factors 2-11). 150 elements × ~7200 states × small set sizes = fast.
- **Edge cases handled:** x=0 (product→0, alt_sum unchanged), starting subsequence with x>limit (goes to dp_over), k=0 achievable via [a,a], all-zero array, limit=1.
- **Stress test verified:** [3,7,10,9,9,0], k=-4, limit=2 → dp_over[0] gets -4 after processing 7 (3-7=-4, product 21>2), then 0 converts it to dp_zero[1] with s=-4. Answer=0. ✓

