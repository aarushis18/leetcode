class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[(i + 1)]:
                return True
        return False

#       dup = {}
#        for i in nums:
#            if i in dup:
 #               return True
            #else:
             #   dup[i] = True

      #  return False
