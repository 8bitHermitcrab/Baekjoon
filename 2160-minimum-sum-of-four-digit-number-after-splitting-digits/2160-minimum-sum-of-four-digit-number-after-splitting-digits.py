class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted(str(num))
        print(s)
        return int(s[0] + s[2]) + int(s[1] + s[3])