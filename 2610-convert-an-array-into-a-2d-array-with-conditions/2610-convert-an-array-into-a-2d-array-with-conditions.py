class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cnt = [0] * (len(nums) + 1)
        
        for num in nums:
            cnt[num] += 1
            if cnt[num] > len(ans):
                ans.append([])
            ans[cnt[num] - 1].append(num)
        return ans