class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        min_idx = 0
        max_idx = len(s)
        ans = []
        
        for i in range(len(s)):
            if s[i] == 'I':
                ans.append(min_idx)
                min_idx += 1
            else:
                ans.append(max_idx)
                max_idx -= 1
        ans.append(min_idx)
        return ans
        