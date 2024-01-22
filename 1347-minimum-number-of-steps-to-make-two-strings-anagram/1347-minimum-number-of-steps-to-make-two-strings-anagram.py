class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = dict()
        cnt = 0
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
            
        for j in t:
            if j in s_dict:
                s_dict[j] -= 1
                
                if s_dict[j] < 0:
                    cnt += 1 
            else:
                cnt += 1
        return cnt