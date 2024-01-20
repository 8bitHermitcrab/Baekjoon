class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1, s2 = set(nums1), set(nums2) 
        return [sum(i in s2 for i in nums1), sum(i in s1 for i in nums2)]