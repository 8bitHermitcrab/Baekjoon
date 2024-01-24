class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        s_list = list(s.split())
        print(s_list)
        for i in s_list:
            ans += i[::-1] + ' '
        return ans.strip()