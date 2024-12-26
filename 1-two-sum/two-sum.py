class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, j in enumerate(nums):
            difference = target - j
            if difference not in sums:
                sums[j] = i
            else:
                return [sums[difference], i]

            
