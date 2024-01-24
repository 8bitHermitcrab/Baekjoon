class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                right.insert(0, i)
        return left + right