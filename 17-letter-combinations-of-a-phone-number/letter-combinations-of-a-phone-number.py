class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # backtracking approach
        res = []

        # create number to letter map:
        digToLet = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curr):
            # when the current string we're builing is as long as the input string, 
            # we've chosen one letter per digit, and we record it.
            if len(curr) == len(digits):
                res.append(curr)
                return
            # try every letter for the current digit and then move to the next digit
            for letter in digToLet[digits[i]]:
                backtrack(i + 1, curr + letter)

        if digits:
            backtrack(0, "")
        return res