from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        ans = -1
        for num in counter:
            if counter[num] == 1:
                ans = max(ans, num)

        return ans
