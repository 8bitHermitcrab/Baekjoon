class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        nums2.sort()
        
        for i in nums1:
            idx = bisect.bisect_left(nums2, i)
            if len(nums2) > idx and nums2[idx] == i:
                ans.add(i)
        return ans