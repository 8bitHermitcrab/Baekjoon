class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        
        for i, j in points:
            dist = (i**2) + (j**2)
            heap.append([dist, i, j])
        heapq.heapify(heap)
        
        while k > 0:
            dist, i, j = heapq.heappop(heap)
            ans.append([i, j])
            k -= 1
        return ans