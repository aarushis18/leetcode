class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_prof = 0

        for num in prices:
            if (num - low) >= max_prof:
                max_prof = num - low
            if num < low:
                low = num
        
        return max_prof