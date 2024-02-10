# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        val_dict = defaultdict(int)
        
        def dfs(node, depth, val_dict):
            if not node:
                return 0
            
            val_dict[depth] += node.val
            dfs(node.left, depth + 1, val_dict)
            dfs(node.right, depth + 1, val_dict)
        
        dfs(root, 0, val_dict)
        max_depth = max(val_dict.keys())
        return val_dict[max_depth]