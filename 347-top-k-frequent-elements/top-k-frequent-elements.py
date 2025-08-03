class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:                           
            freq[num] = freq.get(num, 0) + 1

        # create an array of arrays with the freq of values
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in freq.items():  
            buckets[c].append(num)
        
        ans = []
        for val in range(len(buckets) - 1, 0, -1):
            for num in buckets[val]:
                ans.append(num)
                if len(ans) == k:
                    return ans