class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        s_list = list(s.split())
        for i in s_list:
            ans += i[::-1] + ' '
        return ans.strip()