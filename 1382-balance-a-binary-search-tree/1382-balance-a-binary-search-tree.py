# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        
        def bst(nums):
            if not nums:
                return
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = bst(nums[:mid])
            node.right = bst(nums[mid + 1:])
            return node
        
        inorder(root)
        return bst(nums)