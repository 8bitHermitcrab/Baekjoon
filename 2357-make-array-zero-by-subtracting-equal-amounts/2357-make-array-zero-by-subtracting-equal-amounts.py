class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = {i for i in nums if i}
        return len(s)