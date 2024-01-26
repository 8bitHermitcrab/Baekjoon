class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        left = 0
        right = len(s) - 1
        
        while left < right:
            min_char = min(s_list[left], s_list[right])
            s_list[left] = min_char
            s_list[right] = min_char
            left += 1
            right -= 1
        return ''.join(s_list)