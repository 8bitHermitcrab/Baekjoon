class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        idx = 0
        res = ""
        
        while idx < len(s):
            if s[idx] == '(':
                stack.append(idx)
            elif s[idx] == ')':
                idx_remove = stack.pop()
                if not stack:
                    res += s[idx_remove+1:idx]
            idx += 1
        return res      
                