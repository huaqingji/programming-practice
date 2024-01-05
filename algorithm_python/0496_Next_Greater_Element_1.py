class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # for nums2
        # monotonic decreasing stack
        # backwards
        nums2_next_greater = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            curr_val = nums2[i]
            while stack and curr_val >= stack[-1]:
                stack.pop()
            nums2_next_greater[curr_val] = stack[-1] if stack else -1
            stack.append(curr_val)
        
        # for nums1
        ans = []
        for num1 in nums1:
            ans.append(nums2_next_greater[num1])

        return ans




        