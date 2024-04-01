class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if self.possible(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    def possible(self, weights: List[int], days: int, capacity: int) -> bool:
        cur_weight = 0
        
        for i in weights:
            if (i + cur_weight) > capacity:
                days -= 1
                cur_weight = 0
            cur_weight += i
        return days > 0
        