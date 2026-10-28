from collections import deque
import sys

def solve():
    n = int(sys.stdin.readline().strip())
    S = sys.stdin.readline().strip()
    T = sys.stdin.readline().strip()
    
    if S == T:
        print(0)
        return
    
    start = S
    visited = {start}
    queue = deque([(start, 0)])
    
    while queue:
        curr, dist = queue.popleft()
        
        present = set(curr)
        for x in present:
            for y in range(26):
                cy = chr(ord('a') + y)
                if cy == x:
                    continue
                
                new_s = curr.replace(x, cy)
                
                if new_s == T:
                    print(dist + 1)
                    return
                
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append((new_s, dist + 1))
    
    print(-1)

solve()
