# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:       
        def dfs(node, total):
            if node:
                total = dfs(node.right, total)
                total += node.val
                node.val = total
                total = dfs(node.left, total)
            return total
        
        dfs(root, 0)
        return root