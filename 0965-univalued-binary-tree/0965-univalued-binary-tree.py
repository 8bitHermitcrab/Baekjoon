# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:   
        if root is None:
            return True
        
        stack = [root]
        value = root.val
        
        while stack:
            node = stack.pop(0)
            
            if node.val != value:
                return False
            
            if node.left is not None:
                stack.append(node.left)
            
            if node.right is not None:
                stack.append(node.right)
        
        return True