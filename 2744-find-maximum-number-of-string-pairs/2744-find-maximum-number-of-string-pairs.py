class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt = 0
        words_dict = {}
        for i in words:
            if ''.join(reversed(i)) in words_dict:
                cnt += 1
            words_dict[i] = 1
        return cnt