import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx]); idx += 1
        K = int(data[idx]); idx += 1
        cakes = []
        for i in range(N):
            x = int(data[idx]); idx += 1
            y = int(data[idx]); idx += 1
            z = int(data[idx]); idx += 1
            cakes.append((x, y, z))
        
        indexed = [(max(cakes[i]), i) for i in range(N)]
        indexed.sort(reverse=True)
        
        top2k = [indexed[i][1] for i in range(2 * K)]
        rest = [indexed[i][1] for i in range(2 * K, N)]
        
        TOTAL = sum(indexed[i][0] for i in range(2 * K))
        
        assign = {}
        for i in top2k:
            x, y, z = cakes[i]
            m = max(x, y, z)
            if x == m:
                assign[i] = 0
            elif y == m:
                assign[i] = 1
            else:
                assign[i] = 2
        
        cnt = [0, 0, 0]
        for i in top2k:
            cnt[assign[i]] += 1
        
        odd_dims = [d for d in range(3) if cnt[d] % 2 == 1]
        
        if len(odd_dims) == 0:
            results.append(str(TOTAL))
            continue
        
        a, b = odd_dims[0], odd_dims[1]
        c = 3 - a - b
        
        def get_val(cake, dim):
            if dim == 0: return cake[0]
            elif dim == 1: return cake[1]
            else: return cake[2]
        
        INF = float('inf')
        min_m_a = INF
        min_mb_a = INF
        min_mc_a = INF
        min_m_b = INF
        min_ma_b = INF
        min_mc_b = INF
        
        for i in top2k:
            m = max(cakes[i])
            d = assign[i]
            if d == a:
                if m < min_m_a: min_m_a = m
                cost_b = m - get_val(cakes[i], b)
                if cost_b < min_mb_a: min_mb_a = cost_b
                cost_c = m - get_val(cakes[i], c)
                if cost_c < min_mc_a: min_mc_a = cost_c
            elif d == b:
                if m < min_m_b: min_m_b = m
                cost_a = m - get_val(cakes[i], a)
                if cost_a < min_ma_b: min_ma_b = cost_a
                cost_c = m - get_val(cakes[i], c)
                if cost_c < min_mc_b: min_mc_b = cost_c
        
        max_a_unsel = -1
        max_b_unsel = -1
        max1_c_unsel = -1
        max2_c_unsel = -1
        
        for i in rest:
            va = get_val(cakes[i], a)
            vb = get_val(cakes[i], b)
            vc = get_val(cakes[i], c)
            if va > max_a_unsel: max_a_unsel = va
            if vb > max_b_unsel: max_b_unsel = vb
            if vc > max1_c_unsel:
                max2_c_unsel = max1_c_unsel
                max1_c_unsel = vc
            elif vc > max2_c_unsel:
                max2_c_unsel = vc
        
        fix = INF
        
        if min_mb_a < INF:
            fix = min(fix, min_mb_a)
        if min_ma_b < INF:
            fix = min(fix, min_ma_b)
        if rest and min_m_a < INF:
            fix = min(fix, min_m_a - max_b_unsel)
        if rest and min_m_b < INF:
            fix = min(fix, min_m_b - max_a_unsel)
        if min_mc_a < INF and min_mc_b < INF:
            fix = min(fix, min_mc_a + min_mc_b)
        if len(rest) >= 2 and min_m_a < INF and min_m_b < INF:
            fix = min(fix, min_m_a + min_m_b - max1_c_unsel - max2_c_unsel)
        if rest and min_m_a < INF and min_mc_b < INF:
            fix = min(fix, min_m_a + min_mc_b - max1_c_unsel)
        if rest and min_m_b < INF and min_mc_a < INF:
            fix = min(fix, min_m_b + min_mc_a - max1_c_unsel)
        
        results.append(str(TOTAL - fix))
    
    sys.stdout.write('\n'.join(results) + '\n')

solve()
