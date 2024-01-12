class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = 0
        idx = {}
        
        for i in range(len(garbage)-1, 0, -1):
            for j in garbage[i]:
                idx[j] = idx.get(j, 0) + 1
            
            if idx.get('G'):
                total += travel[i-1]
            if idx.get('P'):
                total += travel[i-1]
            if idx.get('M'):
                total += travel[i-1]
        return total + len(garbage[0]) + idx.get('G', 0) + idx.get('P', 0) + idx.get('M', 0)
        