# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(root, p, g):
            if not root:
                return
            if g and g % 2 == 0:
                self.ans += root.val
            dfs(root.left, root.val, p)
            dfs(root.right, root.val, p)
        
        dfs(root, 0, 0)
        return self.ans