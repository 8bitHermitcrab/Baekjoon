class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        cnt = 0

        for i in s:
            if i == '(':
                stack.append(i)
                if len(stack) > cnt:
                    cnt = len(stack)
            elif i == ')':
                stack.pop()
        return cnt