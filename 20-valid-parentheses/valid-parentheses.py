class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'(':')', '{':'}','[':']'} # add a dict of possible pairs

        stack = []

        for par in s:
            if par in parens:
                stack.append(par)
            elif len(stack) == 0 or parens[stack.pop()] != par:
                return False
        
        return len(stack) == 0