from typing import List

class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return (nums[0] + k) * cost[0]
        
        # Prefix sums (1-indexed): P[i] = sum(nums[0..i-1]), C[i] = sum(cost[0..i-1])
        P = [0] * (n + 1)
        C = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]
            C[i + 1] = C[i] + cost[i]
        
        # dp_prev[i] = min cost to partition first i elements into (m-1) subarrays
        # Base: m=1, dp[1][i] = (P[i] + k) * C[i]
        dp_prev = [0] * (n + 1)
        for i in range(1, n + 1):
            dp_prev[i] = (P[i] + k) * C[i]
        
        answer = dp_prev[n]
        
        for m in range(2, n + 1):
            # dp_curr[i] = min cost to partition first i elements into m subarrays
            # Transition: dp_curr[i] = (P[i]+k*m)*C[i] + min_j { (-C[j])*x + dp_prev[j] }
            # where x = P[i]+k*m, j ranges from m-1 to i-1
            # Lines: y = (-C[j])*x + dp_prev[j], slopes strictly decreasing, x strictly increasing
            
            dp_curr = [0] * (n + 1)
            hull = []  # list of (slope, intercept), slopes strictly decreasing
            front = 0
            
            for i in range(m, n + 1):
                # Add line for j = i-1 (newly available split point)
                j = i - 1
                new_slope = -C[j]
                new_intercept = dp_prev[j]
                
                # Pop from back while the second-to-last line is redundant
                while len(hull) - front >= 2:
                    m_a, b_a = hull[-2]
                    m_b, b_b = hull[-1]
                    # m_a > m_b > new_slope (strictly decreasing slopes)
                    # m_b is redundant if intersection(L_a, new) <= intersection(L_a, L_b)
                    # i.e., (new_intercept - b_a)*(m_a - m_b) <= (b_b - b_a)*(m_a - new_slope)
                    if (new_intercept - b_a) * (m_a - m_b) <= (b_b - b_a) * (m_a - new_slope):
                        hull.pop()
                    else:
                        break
                hull.append((new_slope, new_intercept))
                
                # Query at x = P[i] + k*m (strictly increasing)
                x = P[i] + k * m
                # Pop from front while front line is strictly worse than next at x
                while len(hull) - front >= 2:
                    m_a, b_a = hull[front]
                    m_b, b_b = hull[front + 1]
                    # front is worse if m_a*x + b_a > m_b*x + b_b
                    # i.e., (m_a - m_b)*x > b_b - b_a  (m_a - m_b > 0)
                    if (m_a - m_b) * x > b_b - b_a:
                        front += 1
                    else:
                        break
                
                m_best, b_best = hull[front]
                val = m_best * x + b_best
                dp_curr[i] = x * C[i] + val
            
            answer = min(answer, dp_curr[n])
            dp_prev = dp_curr
        
        return answer
