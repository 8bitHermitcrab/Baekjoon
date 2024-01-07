class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        cnt = 0
        
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] + nums[j]) < target:
                    cnt += 1
        return cnt
        