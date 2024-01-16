class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s_list = []
        start_alp, end_alp = ord(s[0]), ord(s[-2])
        start_num, end_num = int(s[1]), int(s[-1])
        
        for i in range(start_alp, end_alp+1):
            for j in range(start_num, end_num+1):
                s_list.append(chr(i) + str(j))
        return s_list