# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node: Optional[TreeNode], max_val: int, min_val: int):
            if not node:
                return abs(max_val - min_val)
            if max_val < node.val:
                max_val = node.val
            if min_val > node.val:
                min_val = node.val
            
            left = dfs(node.left, max_val, min_val)
            right = dfs(node.right, max_val, min_val)
            return max(left, right)
        
        return dfs(root, root.val, root.val)