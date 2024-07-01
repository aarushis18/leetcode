class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for ind, x in enumerate(nums[:-1]):
            if nums[ind] == nums[ind + 1]:
                return True
        
        return False

        # O(N) time complexity due to iterating through every value in nums (at worst)
        # O(1) space complexity