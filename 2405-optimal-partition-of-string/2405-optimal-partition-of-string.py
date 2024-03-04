class Solution:
    def partitionString(self, s: str) -> int:
        case = []
        ans = 0
        
        for i in range(len(s)):
            if s[i] not in case:
                case.append(s[i])
            else:
                ans += 1
                case.clear()
                case.append(s[i])
        ans += 1
        return ans