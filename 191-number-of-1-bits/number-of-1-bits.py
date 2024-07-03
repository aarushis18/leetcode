class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            if (n >> i) & 1:
                count += 1
        
        return count

        # O(1) time complexity since we will always only iterate through 32 bits at most
        # O(1) space complexity since it remains constant regardless of the number of bits

        