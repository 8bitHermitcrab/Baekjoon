class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)
        
        for _ in range(k):
            square = int(sqrt(-heapq.heappop(heap)))
            heapq.heappush(heap, -square)
        return -sum(heap)