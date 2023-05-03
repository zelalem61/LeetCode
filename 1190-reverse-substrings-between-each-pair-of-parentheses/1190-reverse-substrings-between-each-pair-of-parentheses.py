class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                newStack = []
                while (stack[-1] != '('):
                    newStack.append(stack.pop())
                stack.pop()
                stack = stack + newStack
                
        return ''.join(stack)