class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        nums = defaultdict(int)
        
        for i in arr:
            nums[i] += 1
        
        nums = sorted(nums.items(), key=lambda x: x[1], reverse=True)
        
        cnt = 0
        ans = 0
        
        for key, value in nums:
            cnt += value
            ans += 1
            
            if cnt >= (n / 2):
                return ans