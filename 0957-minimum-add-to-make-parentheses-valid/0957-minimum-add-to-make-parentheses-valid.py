class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        count = 0
        for i in s:
            
            if i == '(':
                stack.append(i)
                print(stack)
            if i == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
                print(stack)
        return len(stack)