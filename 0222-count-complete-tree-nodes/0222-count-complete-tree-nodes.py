# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def count(root: Optional[TreeNode]):
            if root == None:
                return 0
            return count(root.left) + count(root.right) + 1
        
        left = 0
        right = 0
        rl = rr = root
        
        while rl != None:
            rl = rl.left
            left += 1
        while rr != None:
            rr = rr.right
            right += 1
        return count(root) if left != right else (2 ** left) - 1