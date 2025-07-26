class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        l = 0
        max_freq = 0
        best = 0

        for r, ch in enumerate(s):
            idx = ord(ch) - ord('A')
            counts[idx] += 1
            max_freq = max(max_freq, counts[idx])

            while (r - l + 1) - max_freq > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best