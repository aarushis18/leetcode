class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set(nums)

        if len(set_of_nums) == len(nums):
            return False
        else:
            return True

        # O(1) for time complexity since we go through each value in nums once
        # O(1) for memory since we create a map with values from nums