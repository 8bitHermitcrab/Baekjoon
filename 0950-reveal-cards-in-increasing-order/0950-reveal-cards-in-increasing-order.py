class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        que = deque(range(len(deck)))
        ans = [0] * len(deck)
        
        for card in deck:
            ans[que.popleft()] = card
            
            if que:
                que.append(que.popleft())
        return ans