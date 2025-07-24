class TimeMap:
    def __init__(self):
        self.stamps: defaultdict[str, list[tuple[str, int]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.stamps.get(key, [])  # get the values for that timestamp

        if not arr:
            return ""

        left = 0
        right = len(arr) - 1

        ans = ""

        while left <= right:
            mid = (right + left) // 2
            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
