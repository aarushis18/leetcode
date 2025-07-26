class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        need = Counter(t)     # counts still needed for each char
        missing = len(t)      # total chars (with duplicates) still missing

        best_len = float("inf")
        best_l = 0
        l = 0

        for r, c in enumerate(s):
            # include s[r] in the window
            if need[c] > 0:
                missing -= 1
            need[c] -= 1

            # when valid, try to shrink from the left
            while missing == 0:
                # update best window
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l

                # pop s[l] from the window
                left_char = s[l]
                need[left_char] += 1
                if need[left_char] > 0:   # we made the window invalid
                    missing += 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]