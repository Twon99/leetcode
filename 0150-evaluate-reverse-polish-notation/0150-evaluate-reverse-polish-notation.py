class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:

            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                i, j = stack.pop(), stack.pop()
                stack.append(j - i)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                i, j = stack.pop(), stack.pop()
                stack.append(int(float(j) / i))
            else:
                stack.append(int(c))
        return stack[0]


            