import sys

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    
    def kth(self, k):
        pos = 0
        bitmask = 1 << (self.n.bit_length() - 1)
        while bitmask:
            if pos + bitmask <= self.n and self.tree[pos + bitmask] < k:
                pos += bitmask
                k -= self.tree[pos]
            bitmask >>= 1
        return pos + 1

def solve():
    data = sys.stdin.buffer.read().split()
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    if N % 2 == 0:
        B = sorted(A)
        m = N // 2
        ans = sum(B[m:]) - sum(B[:m])
        print(ans)
        return
    
    # Odd N: one element is the "barrier"; left and right parts must be matched independently
    # Coordinate compression
    sorted_vals = sorted(set(A))
    comp_map = {v: i + 1 for i, v in enumerate(sorted_vals)}
    compressed = [comp_map[a] for a in A]
    val = [0] + sorted_vals  # 1-indexed
    n_comp = len(sorted_vals)
    
    # Left pass: for each odd f (1-indexed), left part is A[0..f-2], length f-1
    left_score = [0] * (N + 1)
    count_bit = BIT(n_comp)
    sum_bit = BIT(n_comp)
    total_left = 0
    added = 0
    
    for f in range(1, N + 1, 2):
        target = f - 1
        while added < target:
            c = compressed[added]
            count_bit.update(c, 1)
            sum_bit.update(c, A[added])
            total_left += A[added]
            added += 1
        
        k = (f - 1) // 2
        if k == 0:
            left_score[f] = 0
        else:
            pos = count_bit.kth(k)
            sum_below = sum_bit.query(pos - 1)
            count_below = count_bit.query(pos - 1)
            sum_k_smallest = sum_below + (k - count_below) * val[pos]
            left_score[f] = total_left - 2 * sum_k_smallest
    
    # Right pass: for each odd f (1-indexed), right part is A[f..N-1], length N-f
    right_score = [0] * (N + 1)
    count_bit_r = BIT(n_comp)
    sum_bit_r = BIT(n_comp)
    total_right = 0
    added_r = 0
    
    for f in range(N, 0, -2):
        target_r = N - f
        while added_r < target_r:
            idx = N - 1 - added_r
            c = compressed[idx]
            count_bit_r.update(c, 1)
            sum_bit_r.update(c, A[idx])
            total_right += A[idx]
            added_r += 1
        
        k = (N - f) // 2
        if k == 0:
            right_score[f] = 0
        else:
            pos = count_bit_r.kth(k)
            sum_below = sum_bit_r.query(pos - 1)
            count_below = count_bit_r.query(pos - 1)
            sum_k_smallest = sum_below + (k - count_below) * val[pos]
            right_score[f] = total_right - 2 * sum_k_smallest
    
    ans = 0
    for f in range(1, N + 1, 2):
        s = left_score[f] + right_score[f]
        if s > ans:
            ans = s
    print(ans)

solve()
