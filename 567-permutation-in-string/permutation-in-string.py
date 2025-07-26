class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        need = Counter(s1)
        win = Counter(s2[:n])
        if win == need:
            return True

        for r in range(n, m):
            add = s2[r]
            rem = s2[r - n]
            win[add] += 1
            win[rem] -= 1
            if win[rem] == 0:
                del win[rem]
            if win == need:
                return True

        return False
