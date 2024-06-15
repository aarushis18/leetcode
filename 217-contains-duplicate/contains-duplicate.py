class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_to_index = {}

        for index, num in enumerate(nums):
            if num in num_to_index:
                return True

            num_to_index[num] = index
        
        return False

        # O(N) for time complexity since we go through each value in nums once
        # O(N) for memory since we create a map with values from nums
            