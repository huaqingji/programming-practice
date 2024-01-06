class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def backtrack(path, used):
            nonlocal nums, ans
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i, num in enumerate(nums):
                if not used[i]:
                    path.append(num)
                    used[i] = True
                    backtrack(path, used)
                    path.pop()
                    used[i] = False

        path = []
        used = [False] * len(nums)
        backtrack(path, used)
        return ans