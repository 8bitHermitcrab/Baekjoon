class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def search(key):
            left, res, cnt = 0, 0, 0
            
            for right, x in enumerate(answerKey):
                if x == key:
                    cnt += 1
                
                while cnt > k:
                    if answerKey[left] == key:
                        cnt -= 1
                    left += 1
                
                res = max(res, right - left + 1)
            return res
        return max(search("T"), search("F"))