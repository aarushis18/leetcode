class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)

        for letter in s:
            letters[letter] += 1
        
        for letter in t:
            letters[letter] -= 1
        
        for letter in letters.values():
            if letter != 0:
                return False
    
        return True

        # O(n) time complexity due to for loops
        # O(n) memory complexity due to hash map   