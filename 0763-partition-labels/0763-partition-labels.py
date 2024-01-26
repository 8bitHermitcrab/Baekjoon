class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        idx = {}
        size, end = 0, 0
        
        for i, c in enumerate(s):
            idx[c] = i
        
        for i, c in enumerate(s):
            size += 1
            if idx[c] > end:
                end = idx[c]
            end = max(end, idx[c])
            
            if i == end:
                ans.append(size)
                size = 0
        return ans