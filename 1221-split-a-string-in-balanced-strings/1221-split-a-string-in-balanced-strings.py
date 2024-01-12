class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        r_cnt = 0
        l_cnt = 0
        
        for i in s:
            if i == 'R':
                r_cnt += 1
            else:
                l_cnt += 1
                
            if r_cnt == l_cnt:
                cnt += 1
        return cnt