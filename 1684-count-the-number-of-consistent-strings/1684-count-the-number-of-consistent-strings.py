class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        for word in words:
            for i in word:
                if not i in allowed:
                    cnt += 1
                    break
        return len(words) - cnt