class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set() # using a set since we only want each value in there once

        for num in nums:
            if num in unique_nums:
                return True

            unique_nums.add(num)
        
        return False

        # O(N) for time complexity since we go through each value in nums once
        # O(N) for memory since we create a map with values from nums
            