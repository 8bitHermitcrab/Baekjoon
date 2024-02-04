class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = sum(nums[i] for i in range(0, len(nums), 2))
        return ans