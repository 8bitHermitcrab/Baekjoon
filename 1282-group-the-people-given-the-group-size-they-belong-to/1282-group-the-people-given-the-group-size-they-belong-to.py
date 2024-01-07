class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans, group, next_group = [], [], []
        
        for i, j in enumerate(groupSizes):
            group.append([j, i])
        group.sort()
        
        for length, index in group:
            next_group.append(index)
            if len(next_group) == length:
                ans.append(next_group)
                next_group = []
        return ans