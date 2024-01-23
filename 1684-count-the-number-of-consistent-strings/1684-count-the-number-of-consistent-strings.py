class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        set_allow = set(allowed)
        
        for word in words:
            if set(word).union(set_allow) == set_allow:
                cnt += 1
        return cnt