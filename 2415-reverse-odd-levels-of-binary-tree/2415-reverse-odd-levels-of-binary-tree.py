# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode], odd: bool) -> None:
            if not left:
                return
        
            if odd:
                left.val, right.val = right.val, left.val
            dfs(left.left, right.right, not odd)
            dfs(left.right, right.left, not odd)
                
        dfs(root.left, root.right, True)
        return root
            