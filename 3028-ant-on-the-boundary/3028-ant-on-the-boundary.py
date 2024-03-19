class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        
        for num in nums:
            l += num
            if l == 0:
                ans += 1
        return ans