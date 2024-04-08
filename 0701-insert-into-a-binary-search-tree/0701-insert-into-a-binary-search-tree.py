# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
        else:
            self.insert(root, val)
        return root
    
    def insert(self, root: Optional[TreeNode], val: int) -> None:
        if root.val > val:
            if root.left:
                self.insert(root.left, val)
            else:
                root.left = TreeNode(val)
        elif root.val < val:
            if root.right:
                self.insert(root.right, val)
            else:
                root.right = TreeNode(val)