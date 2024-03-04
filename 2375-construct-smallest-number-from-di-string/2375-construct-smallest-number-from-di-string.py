class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N = len(pattern)
        L = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        result = ''
        
        for i, c in enumerate(pattern):
            if c == 'I':
                result += L.pop(0)
            elif c == 'D':
                j = i
                cnt = 1
                
                while j+1 < N and pattern[j+1] == 'D':
                    cnt += 1
                    j += 1
                result += L.pop(cnt)
        result += L.pop(0)
        return result