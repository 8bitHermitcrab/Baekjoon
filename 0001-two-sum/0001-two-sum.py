class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        left, right = 0, 0
        
        for i in range(len(nums)):
            left = nums[i]
            for j in range(i):
                right = nums[j]
                if left + right == target:
                    result.append(j)
                    result.append(i)
        return result