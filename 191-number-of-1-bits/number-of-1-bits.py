class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            if (n >> i) & 1:
                count += 1

        return count

        # O(1) time complexity since we always only go through 32 bits
        # O(1) space complexity since we are only using simple variables, no data structures
