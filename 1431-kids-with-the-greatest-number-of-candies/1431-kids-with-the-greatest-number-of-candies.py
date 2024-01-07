class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_kid = max(candies)
        
        for i in candies:
            if (i + extraCandies) < max_kid:
                ans.append(False)
            else:
                ans.append(True)
        return ans
        