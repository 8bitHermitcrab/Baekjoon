class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        result = ''
        
        for i, c in enumerate(pattern):
            if c == 'I':
                result += l.pop(0)
            elif c == 'D':
                j = i
                cnt = 1
                
                while j+1 < n and pattern[j+1] == 'D':
                    cnt += 1
                    j += 1
                result += l.pop(cnt)
        result += l.pop(0)
        return result