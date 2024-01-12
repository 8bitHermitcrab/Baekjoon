class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cnt = 0
        total = 0
        
        for i in bank:
            cur_cnt = i.count('1')
            if cur_cnt > 0:
                total += cnt * cur_cnt
                cnt = cur_cnt
        return total