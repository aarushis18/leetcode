class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if len(stack) == 0:
                stack.append(p)
                
            elif p in '{[(':
                stack.append(p)

            elif p in '}])':
                if stack[-1] == '(' and p == ')':
                    stack.pop()
                elif stack[-1] == '{' and p == '}':
                    stack.pop()
                elif stack[-1] == '[' and p == ']':
                    stack.pop()
                else:
                    return False

            else:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False

    # Space Complexity: O(N) since the stack could grow as large as the input string is
    # Time Complexity: O(N) since we iterate through each value in the input string


