class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        i = 0
        final = []

        for _ in range(k):
            most_freq = max(freq, key=freq.get)
            final.append(most_freq)
            del freq[most_freq]

        return final