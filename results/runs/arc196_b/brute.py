import sys
from itertools import product

def solve():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    MOD = 998244353
    results = []
    for _ in range(T):
        H = int(data[idx]); W = int(data[idx+1]); idx += 2
        grid = []
        for i in range(H):
            grid.append(data[idx])
            idx += 1

        def get_sides(tile_type, rot):
            if tile_type == 'A':
                if rot == 0: return {0, 1}  # top, right
                if rot == 1: return {1, 2}  # right, bottom
                if rot == 2: return {2, 3}  # bottom, left
                if rot == 3: return {3, 0}  # left, top
            else:
                if rot == 0: return {0, 2}  # top, bottom
                if rot == 1: return {1, 3}  # left, right

        num_choices = []
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 'A':
                    num_choices.append(4)
                else:
                    num_choices.append(2)

        count = 0
        for combo in product(*[range(n) for n in num_choices]):
            valid = True
            for i in range(H):
                for j in range(W):
                    if not valid:
                        break
                    k = i * W + j
                    sides = get_sides(grid[i][j], combo[k])
                    # Check horizontal: right of (i,j) vs left of (i,(j+1)%W)
                    right_ij = 1 in sides
                    k2 = i * W + ((j + 1) % W)
                    sides2 = get_sides(grid[i][(j+1) % W], combo[k2])
                    left_next = 3 in sides2
                    if right_ij != left_next:
                        valid = False
                        break
                    # Check vertical: bottom of (i,j) vs top of ((i+1)%H, j)
                    bottom_ij = 2 in sides
                    k3 = ((i + 1) % H) * W + j
                    sides3 = get_sides(grid[(i+1) % H][j], combo[k3])
                    top_below = 0 in sides3
                    if bottom_ij != top_below:
                        valid = False
                        break
            if valid:
                count = (count + 1) % MOD

        results.append(str(count))

    print('\n'.join(results))

solve()
