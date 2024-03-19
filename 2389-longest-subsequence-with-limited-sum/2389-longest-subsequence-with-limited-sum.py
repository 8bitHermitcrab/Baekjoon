class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        for query in queries:
            idx = bisect.bisect(nums, query)
            ans.append(idx)
        return ans