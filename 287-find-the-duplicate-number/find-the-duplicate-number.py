class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]       # slow increments at single speed
            fast = nums[nums[fast]] # fast increments at double speed

            if slow == fast:        # slow caught up to fast, and they're equal
                break

        new_slow = 0
        while True:
            slow = nums[slow]       # continue incrementing from where slow was
            new_slow = nums[new_slow]

            if slow == new_slow:
                return slow