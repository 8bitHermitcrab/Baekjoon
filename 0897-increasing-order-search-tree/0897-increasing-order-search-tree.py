# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        lfs = self.lfs(root)
        ans = lfs[0]
        
        for i in range(len(lfs)-1):
            lfs[i].left = None
            lfs[i].right = lfs[i+1]
        lfs[-1].left = None
        return ans
        
    def lfs(self, root: TreeNode) -> TreeNode:
        if not root:
            return []
        return self.lfs(root.left) + [root] + self.lfs(root.right)