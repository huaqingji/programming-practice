class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        window = 0 # track # of 0 in current window
        left, ans = 0, 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                window += 1
            while window > k and left < right:
                if nums[left] == 0:
                    window -= 1
                left += 1

            if window <= k:
                ans = max(ans, right - left + 1)

        return ans