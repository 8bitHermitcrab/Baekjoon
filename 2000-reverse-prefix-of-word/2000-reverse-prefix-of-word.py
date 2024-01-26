class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            idx = word.index(ch)
            prefix = word[:idx+1][::-1]
            return prefix + word[idx+1:]
        else:
            return word