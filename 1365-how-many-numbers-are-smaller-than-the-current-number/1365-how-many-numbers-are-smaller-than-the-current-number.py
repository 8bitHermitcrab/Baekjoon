class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in nums:
            cnt = [n for n in nums if n < i]
            ans.append(len(cnt))
        return ans