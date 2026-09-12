class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Track ways to reach the last two steps
        prev2 = 1  # Represents f(n-2) -> initially step 1
        prev1 = 2  # Represents f(n-1) -> initially step 2
        
        # Step through the staircase from step 3 up to n
        for _ in range(3, n + 1):
            current = prev1 + prev2  # f(n) = f(n-1) + f(n-2)
            prev2 = prev1            # Move f(n-2) forward
            prev1 = current          # Move f(n-1) forward
            
        return prev1