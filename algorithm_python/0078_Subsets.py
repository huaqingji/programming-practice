class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = []
        def backtrack(path, start):
            nonlocal nums, ans
            ans.append(path[:])
            if len(path) == len(nums):
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        
        path, start = [], 0
        backtrack(path, start)
        return ans
            