class Solution:
    def sortSentence(self, s: str) -> str:
        ans = ''
        s_list = s.split()
        s_list.sort(key=lambda x : x[-1] )
        
        for i in s_list:
            ans += i[:-1] + ' '
        return ans[:-1]