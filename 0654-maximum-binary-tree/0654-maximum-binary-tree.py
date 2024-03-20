# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        max_val, max_idx = max((v, i) for i, v in enumerate(nums))
        
        node = TreeNode(max_val)
        
        left = nums[0:max_idx]
        node.left = self.constructMaximumBinaryTree(left)
        
        right = nums[max_idx+1:]
        node.right = self.constructMaximumBinaryTree(right)
        
        return node