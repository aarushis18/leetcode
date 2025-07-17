class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0

        while left <= right:
            mid_point = (left + right) // 2

            if target > nums[mid_point]:
                left = mid_point + 1

            elif target < nums[mid_point]:
                right = mid_point  - 1

            else:
                return mid_point
        
        return -1