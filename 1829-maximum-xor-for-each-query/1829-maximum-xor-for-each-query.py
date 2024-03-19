class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        m = (1 << maximumBit) - 1
        ans = []
        xors = 0
        
        for num in nums:
            xors ^= num
            ans.append(xors ^ m)
        return ans[::-1]