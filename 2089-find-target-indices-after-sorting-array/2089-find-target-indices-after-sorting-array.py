class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        cnt = nums.count(target)
        n = sum(num < target for num in nums)
        return [i for i in range(n, n+cnt)]