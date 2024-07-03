class Solution:
    def countBits(self, n: int) -> List[int]:
        count = 0
        binaries = []

        while count <= n:
            sec_count = 0
            for j in range(32):
                if (count >> j) & 1:
                    sec_count += 1

            binaries.append(sec_count)
            count += 1
    
        return binaries
        