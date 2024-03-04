class Solution:
    def minTimeToType(self, word: str) -> int:
        sec = 0
        cur = 'a'
        
        for i in word:
            diff = abs(ord(i) - ord(cur))
            sec += min(26 - diff, diff)
            cur = i
        return sec + len(word)