class NumArray:

    def __init__(self, nums: List[int]):   
        self.nums = nums
        
        presum = [nums[0]]
        for i in range(1, len(nums)):
            presum.append(presum[-1] + nums[i])
        self.presum = presum

    def sumRange(self, left: int, right: int) -> int:
        
        return self.presum[right] - self.presum[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)