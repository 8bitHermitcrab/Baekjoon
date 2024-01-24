class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        ans = []
        for i in nums:
            if i > 0:
                positive.append(i)
            else:
                negative.append(i)
        for j in range(len(positive)):
            ans.append(positive[j])
            ans.append(negative[j])
        return ans