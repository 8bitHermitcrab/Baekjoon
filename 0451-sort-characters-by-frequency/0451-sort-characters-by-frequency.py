from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        answer = ''
        
        cnt = Counter(list(s)).most_common()
        
        for i in cnt:
            answer = answer + i[0] * i[1]
        
        return answer