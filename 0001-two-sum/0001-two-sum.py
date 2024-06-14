class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the keys are the complements, the values are the indices
        
        sums = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in sums:
                return [sums[complement], index]
            
            sums[num] = index


        