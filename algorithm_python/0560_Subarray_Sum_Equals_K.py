from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        counter = defaultdict(int)
        counter[0] = 1

        presum, ans = 0, 0
        for num in nums:
            presum += num
            ans += counter[(presum - k)]

            counter[presum] += 1

        return ans