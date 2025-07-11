class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1               # two pointers
        while left < right:
            # move left pointer to next alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # move right pointer to previous alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():  # compare after normalising
                return False

            left  += 1
            right -= 1                               # shrink window

        return True