class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        spaces_cnt = []
        
        for i in sentences:
            spaces_cnt.append(i.count(' ') + 1)
            
        return max(spaces_cnt)