class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {} # complement, index

        for index, x in enumerate(nums):
            diff = target - x

            if diff in sums.keys():
                return [sums[diff], index]
            
            sums[x] = index
        

        



        