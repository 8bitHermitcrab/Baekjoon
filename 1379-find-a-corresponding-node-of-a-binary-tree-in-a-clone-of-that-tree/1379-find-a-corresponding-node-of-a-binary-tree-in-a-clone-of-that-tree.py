# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(origin, clone, target):
            if not origin:
                return
            if origin == target:
                return clone
            return dfs(origin.left, clone.left, target) or dfs(origin.right, clone.right, target)
        
        return dfs(original, cloned, target)