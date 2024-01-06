class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # bottom up
        # improve space complexity
        back_two, back_one = 0, 0
        n = len(cost)
        for i in range(2, n + 1):
            curr = min(back_two + cost[i-2], back_one + cost[i-1])
            back_two, back_one = back_one, curr

        return back_one