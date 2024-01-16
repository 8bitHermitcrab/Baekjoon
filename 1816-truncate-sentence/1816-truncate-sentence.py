class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = ''
        s_list = s.split()
        
        for i in range(k):
            ans += s_list[i] + ' '
        return ans.rstrip()