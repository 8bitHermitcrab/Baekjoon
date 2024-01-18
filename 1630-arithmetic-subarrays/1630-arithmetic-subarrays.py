class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [True] * len(l)
        
        for i in range(len(l)):
            arr = nums[l[i] : r[i]+1]
            arr.sort(reverse=True)
            diff = arr[0] - arr[1]
            for j in range(len(arr)-1):
                if diff != (arr[j] - arr[j+1]):
                    ans[i] = False
                    break
        return ans