class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        even_sum = 0
        odd_sum = 0
        
        for i, a in enumerate(arr):
            curr_even = odd_sum + ((i + 1) // 2 ) * a
            curr_odd = even_sum + (i // 2 + 1) * a
            
            ans += curr_odd
            even_sum = curr_even
            odd_sum = curr_odd
        return ans