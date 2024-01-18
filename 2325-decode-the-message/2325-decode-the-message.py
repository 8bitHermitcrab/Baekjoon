class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ans = ''
        alpha_dict = {' ':' '}
        curr_alpha = 'a'
        for i in key:
            if i not in alpha_dict:
                alpha_dict[i] = curr_alpha
                curr_alpha = chr(ord(curr_alpha) + 1)

        for i in message:
            ans += alpha_dict[i]
        return ans
            