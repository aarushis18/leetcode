import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            fir = heapq.heappop(stones)
            sec = heapq.heappop(stones)

            if sec > fir:
                heapq.heappush(stones, fir - sec)
        
        stones.append(0)
        return abs(stones[0])

        