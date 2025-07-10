class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:                           # ❶ build freq map
            count[num] = count.get(num, 0) + 1

        # --- bucket array indexed by frequency ---
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():               # ❷ fill buckets
            buckets[c].append(num)

        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:                  # stop early
                    return res
