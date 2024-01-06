class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        memo = {}
        def dp(i):
            nonlocal nums, memo
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))

            return memo[i]
            
        return dp(0)