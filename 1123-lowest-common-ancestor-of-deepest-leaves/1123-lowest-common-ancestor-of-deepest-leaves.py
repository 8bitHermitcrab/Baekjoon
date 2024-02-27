# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if node is None:
                return None, 0
            
            l_lca, l_depth = dfs(node.left)
            r_lca, r_depth = dfs(node.right)
            
            if l_depth > r_depth:
                return l_lca, l_depth + 1
            if l_depth < r_depth:
                return r_lca, r_depth + 1
            
            return node, l_depth + 1
        
        return dfs(root)[0]