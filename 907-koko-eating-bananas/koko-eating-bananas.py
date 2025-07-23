class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            k = (low + high) // 2   # koko's banana-per-hour eating speed
            total_hours = 0

            for pile in piles:
                total_hours += (pile + k - 1) // k
                if total_hours > h:
                    break

            if total_hours <= h:
                high = k
            else:
                low = k + 1

        return low