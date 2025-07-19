class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = (len(nums)) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is bigger than the right‑most element,
            # the minimum lies strictly to the right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise the minimum is at mid or to its left.
                right = mid
        
        return nums[left]
