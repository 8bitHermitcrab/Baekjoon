class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = 0
        k_max = 100
        curr_sum = 0
        cnt = [0] * (k_max + 2)
        
        for start, end in nums:
            cnt[start] += 1
            cnt[end + 1] -= 1
        
        for i in range(1, k_max+1):
            curr_sum += cnt[i]
            if curr_sum > 0:
                ans += 1
        return ans