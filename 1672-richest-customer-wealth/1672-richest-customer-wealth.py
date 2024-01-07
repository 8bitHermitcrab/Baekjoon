class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_list = []
        
        for i in accounts:
            sum_list.append(sum(i))

        return max(sum_list)
        