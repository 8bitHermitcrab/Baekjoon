class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        x_arr = nums[:n]
        y_arr = nums[n:]

        for i in range(n):
            ans.append(x_arr[i])
            ans.append(y_arr[i])
        return ans