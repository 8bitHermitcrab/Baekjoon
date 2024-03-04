class Solution:
    def minOperations(self, nums: List[int]) -> int:
        temp = nums[0]
        cnt = 0
        
        if len(nums) == 1:
            return 0
        else:
            for i in range(1, len(nums)):
                if nums[i] <= temp:
                    cnt += ((temp - nums[i]) + 1)
                    nums[i] += ((temp - nums[i]) + 1)
                    temp = nums[i]
                temp = nums[i]
            return cnt