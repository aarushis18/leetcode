class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price = prices[0] 
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - cheapest_price) 
            cheapest_price = min(price, cheapest_price) # updates cheapest_price if current price is cheaper
            
        return max_profit

        # O(N) for time complexity, since we run through each price in prices atleast once
        # O(1) for memory, since we only keep track of the cheapest price, and the maximum profit