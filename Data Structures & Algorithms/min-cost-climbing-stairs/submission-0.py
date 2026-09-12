class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memory={}
        def minimum_cost_to_index(j: int) -> int:
            if j in memory:
                return memory[j]
            if j==0:
                memory[j]=0
                return memory[j]
            if j==1:
                memory[j]=0
                return memory[j]
            if j > 1:
                min_price=0
                min_price=min(minimum_cost_to_index(j-1)+cost[j-1], minimum_cost_to_index(j-2)+cost[j-2])
                memory[j]=min_price
                return memory[j]
        return minimum_cost_to_index(len(cost))
