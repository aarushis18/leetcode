class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        extras = []
        greatest = max(candies)
        
        for kid in candies:
            if kid + extraCandies >= greatest:
                extras.append(True)
            else:
                extras.append(False)
        
        return extras