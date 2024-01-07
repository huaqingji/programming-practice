class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        def binary_search(nums, target, left_bound):
            
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if left_bound:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            if left_bound:
                if left < len(nums) and nums[left] == target:
                    return left
                else:
                    return -1
            else:
                if right >= 0 and nums[right] == target:
                    return right
                else:
                    return -1
        
        first = binary_search(nums, target, left_bound=True)
        last = binary_search(nums, target, left_bound=False)
        return [first, last]