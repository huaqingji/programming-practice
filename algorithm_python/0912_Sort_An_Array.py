class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        temp = [None] * len(nums)

        def merge_sort(nums, left, right):
            if left == right:
                return

            mid = left + (right - left) // 2
            merge_sort(nums, left, mid)
            merge_sort(nums, mid + 1, right)
            merge(nums, left, mid, right)


        def merge(nums, left, mid, right):
            nonlocal temp
            for i in range(left, right + 1):
                temp[i] = nums[i]

            p1, p2 = left, mid + 1
            for i in range(left, right + 1):
                if p1 <= mid and p2 <= right:
                    if temp[p1] <= temp[p2]:
                        nums[i] = temp[p1]
                        p1 += 1
                    else:
                        nums[i] = temp[p2]
                        p2 += 1
                elif p1 <= mid:
                    nums[i] = temp[p1]
                    p1 += 1
                elif p2 <= right:
                    nums[i] = temp[p2]
                    p2 += 1    

    
        merge_sort(nums, 0, len(nums) - 1)
        return nums

    