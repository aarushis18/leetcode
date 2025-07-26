class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        start = 0

        max_len = len(letters)

        for letter in s: 
            while letter in letters:
                letters.remove(s[start])
                start += 1

            letters.add(letter)

            if len(letters) > max_len:
                max_len = len(letters)

        return max_len