class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        piles.sort()
        piles = deque(piles)
        
        while piles:
            piles.pop()
            ans += piles.pop()
            piles.popleft()
        return ans