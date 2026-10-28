### NOTES

The core difficulty is that the "no dead ends on a torus" condition couples every cell to its four neighbors through shared edge-midpoints, creating a global constraint system. The torus wrapping means there is no natural "starting point" to anchor a DP, so naive sequential approaches (row-by-row or column-by-row) must handle the wraparound carefully.

Key structural observation: for each column independently, the bottom-edge state is a deterministic function of the top-edge state (flip for A, pass-through for B). This means the vertical torus consistency reduces to a simple per-column parity condition (even number of A's in each column). The horizontal constraints, however, introduce binary choices (which adjacent edge-pair the A-tile uses) that couple neighboring columns within each row.

After substituting the vertical recurrence into the horizontal constraints, all remaining unknowns reduce to W variables (one per column, representing the top-edge state of row 0). The horizontal constraints per row become XOR equations of the form v_a XOR v_b = c, where a and b are B-positions in that row (cyclically consecutive) and c is a computable constant. The global problem is thus: check consistency of a system of two-variable XOR equations over GF(2), and count free variables.

Pitfalls I identified:
- Self-loops occur when a row has exactly one B; the edge is (p,p) and is consistent only if W is odd.
- Multi-edges: different rows can produce edges between the same pair of column-nodes with potentially different weights (contradiction if they differ).
- All-A rows produce no edges but impose a global W-even requirement; if W is odd and any all-A row exists, the answer is 0.
- The cyclic gap calculation must correctly handle the wraparound edge (from the last B to the first B in the row).
- The rank formula is rank = |V_involved| - |C| where V_involved is the set of nodes appearing in at least one edge and C is the number of connected components among those nodes; the number of free variables is W - rank.

### NEXT

- **Graph XOR constraint system (primary):** Build an undirected graph on W nodes. For each row, list B-positions cyclically; for each consecutive pair (b_j, b_{j+1}) compute the edge weight using the gap and prefix-A-parity values. Run BFS/DFS to check consistency (detect contradictions including self-loops) and compute the number of free variables as W minus rank. Multiply by 2^(number of all-A rows). O(HW) time, O(W) extra space.

- **Row-by-row transfer with per-row satisfiability check:** Process rows sequentially, maintaining the W-bit "top state" as the only inter-row state. For each row, given the top state, verify the horizontal XOR subsystem (in x-variables) is satisfiable — this is a local check on the row's A/B pattern. The torus wraparound (last row connects to first) is handled by requiring the final top state equals the initial one, which reduces to the column parity check. Equivalent to approach 1 but organized differently; useful as a cross-check.

- **Brute-force enumeration for small instances:** For H,W ≤ 4 (so HW ≤ 16), enumerate all 4^a × 2^b placements, check the no-dead-ends condition directly, and count valid ones. Use to validate the formula on random small cases before trusting the general solution.

- **Homology / cycle-space perspective (theoretical sanity check):** The consistent 1-chains on the torus form a subspace of dimension related to the torus's first Betti number (2). Verify that the number of independent global constraints is at most 2 per "direction" of the torus, which provides a sanity bound on the rank and helps detect implementation bugs (e.g., if the computed rank exceeds HW - W, something is wrong).

- **Transpose and re-derive (column-by-column symmetry check):** Swap the roles of rows and columns. The same analysis should apply with H and W swapped (B-tiles pass-through vertically, A-tiles flip). Verify that the answer computed via the row-based approach matches the column-based approach on small cases, confirming no asymmetry bug.
