import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1

    a = [0] * (M + 1)
    b = [0] * (M + 1)
    direction = [0] * (M + 1)

    for i in range(1, M + 1):
        S = int(data[idx]); idx += 1
        T = int(data[idx]); idx += 1
        if S < T:
            a[i] = S; b[i] = T; direction[i] = 1
        else:
            a[i] = T; b[i] = S; direction[i] = -1

    queries = []
    for _ in range(Q):
        L = int(data[idx]); idx += 1
        R = int(data[idx]); idx += 1
        queries.append((L, R))

    prev = [0] * (M + 1)

    # Endpoint conflicts: same start or same end (any direction)
    last_start = [0] * (N + 1)
    last_end = [0] * (N + 1)
    for j in range(1, M + 1):
        aj, bj = a[j], b[j]
        if last_start[aj] > prev[j]:
            prev[j] = last_start[aj]
        if last_end[bj] > prev[j]:
            prev[j] = last_end[bj]
        last_start[aj] = j
        last_end[bj] = j

    # Group by direction for CDQ crossing detection
    dir1 = [(a[i], b[i], i) for i in range(1, M + 1) if direction[i] == 1]
    dir2 = [(a[i], b[i], i) for i in range(1, M + 1) if direction[i] == -1]

    # Segment tree (global, reused)
    seg_size = 1
    while seg_size <= N:
        seg_size <<= 1
    tree = [0] * (2 * seg_size)

    sys.setrecursionlimit(1000000)

    def cdq_A(arr, l, r):
        """Case A: a_i < a_j < b_i < b_j. Maintains arr sorted by a (ascending)."""
        if r - l <= 1:
            return
        mid = (l + r) >> 1
        cdq_A(arr, l, mid)
        cdq_A(arr, mid, r)

        sz = seg_size
        tr = tree
        prev_local = prev
        touched = []
        p = l
        for j_idx in range(mid, r):
            aj, bj, ij = arr[j_idx]
            while p < mid and arr[p][0] < aj:
                bi = arr[p][1]
                ii = arr[p][2]
                pos = bi - 1 + sz
                if ii > tr[pos]:
                    tr[pos] = ii
                    pos >>= 1
                    while pos:
                        lc = tr[pos << 1]
                        rc = tr[(pos << 1) | 1]
                        nv = lc if lc >= rc else rc
                        if tr[pos] >= nv:
                            break
                        tr[pos] = nv
                        pos >>= 1
                touched.append(bi)
                p += 1
            if p > l:
                lo = aj + sz
                hi = bj - 2 + sz
                res = 0
                while lo <= hi:
                    if lo & 1:
                        if tr[lo] > res: res = tr[lo]
                        lo += 1
                    if not (hi & 1):
                        if tr[hi] > res: res = tr[hi]
                        hi -= 1
                    lo >>= 1
                    hi >>= 1
                if res > prev_local[ij]:
                    prev_local[ij] = res
        # Clear touched positions
        for pos in touched:
            p2 = pos - 1 + sz
            tr[p2] = 0
            p2 >>= 1
            while p2:
                lc = tr[p2 << 1]
                rc = tr[(p2 << 1) | 1]
                nv = lc if lc >= rc else rc
                if tr[p2] <= nv:
                    break
                tr[p2] = nv
                p2 >>= 1

        # Merge by a ascending
        n1 = mid - l
        n2 = r - mid
        temp = arr[l:r]
        i1, i2 = 0, 0
        for k in range(n1 + n2):
            if i1 < n1 and (i2 >= n2 or temp[i1][0] <= temp[n1 + i2][0]):
                arr[l + k] = temp[i1]
                i1 += 1
            else:
                arr[l + k] = temp[n1 + i2]
                i2 += 1

    def cdq_B(arr, l, r):
        """Case B: a_j < a_i < b_j < b_i. Maintains arr sorted by b (descending)."""
        if r - l <= 1:
            return
        mid = (l + r) >> 1
        cdq_B(arr, l, mid)
        cdq_B(arr, mid, r)

        sz = seg_size
        tr = tree
        prev_local = prev
        touched = []
        p = l
        for j_idx in range(mid, r):
            aj, bj, ij = arr[j_idx]
            while p < mid and arr[p][1] > bj:
                ai = arr[p][0]
                ii = arr[p][2]
                pos = ai - 1 + sz
                if ii > tr[pos]:
                    tr[pos] = ii
                    pos >>= 1
                    while pos:
                        lc = tr[pos << 1]
                        rc = tr[(pos << 1) | 1]
                        nv = lc if lc >= rc else rc
                        if tr[pos] >= nv:
                            break
                        tr[pos] = nv
                        pos >>= 1
                touched.append(ai)
                p += 1
            if p > l:
                lo = aj + sz
                hi = bj - 2 + sz
                res = 0
                while lo <= hi:
                    if lo & 1:
                        if tr[lo] > res: res = tr[lo]
                        lo += 1
                    if not (hi & 1):
                        if tr[hi] > res: res = tr[hi]
                        hi -= 1
                    lo >>= 1
                    hi >>= 1
                if res > prev_local[ij]:
                    prev_local[ij] = res
        # Clear
        for pos in touched:
            p2 = pos - 1 + sz
            tr[p2] = 0
            p2 >>= 1
            while p2:
                lc = tr[p2 << 1]
                rc = tr[(p2 << 1) | 1]
                nv = lc if lc >= rc else rc
                if tr[p2] <= nv:
                    break
                tr[p2] = nv
                p2 >>= 1

        # Merge by b descending
        n1 = mid - l
        n2 = r - mid
        temp = arr[l:r]
        i1, i2 = 0, 0
        for k in range(n1 + n2):
            if i1 < n1 and (i2 >= n2 or temp[i1][1] >= temp[n1 + i2][1]):
                arr[l + k] = temp[i1]
                i1 += 1
            else:
                arr[l + k] = temp[n1 + i2]
                i2 += 1

    # Run CDQ on each direction (use copies since CDQ rearranges the array)
    if len(dir1) > 1:
        cdq_A(dir1[:], 0, len(dir1))
        cdq_B(dir1[:], 0, len(dir1))
    if len(dir2) > 1:
        cdq_A(dir2[:], 0, len(dir2))
        cdq_B(dir2[:], 0, len(dir2))

    # Sparse table for O(1) range max on prev[1..M]
    LOG = M.bit_length()
    st = [[0] * (M + 2) for _ in range(LOG)]
    for i in range(1, M + 1):
        st[0][i] = prev[i]
    for j in range(1, LOG):
        half = 1 << (j - 1)
        row_j = st[j]
        row_jm1 = st[j - 1]
        for i in range(1, M + 2 - (1 << j)):
            v1 = row_jm1[i]
            v2 = row_jm1[i + half]
            row_j[i] = v1 if v1 >= v2 else v2

    # Answer queries
    out = []
    for L, R in queries:
        if L >= R:
            out.append("Yes")
        else:
            length = R - L
            j = length.bit_length() - 1
            v1 = st[j][L + 1]
            v2 = st[j][R - (1 << j) + 1]
            mx = v1 if v1 >= v2 else v2
            out.append("No" if mx >= L else "Yes")

    sys.stdout.write('\n'.join(out) + '\n')

main()
