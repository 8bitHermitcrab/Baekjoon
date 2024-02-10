# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return (0, 0)
            
            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)
            total_cnt = 1 + left_cnt + right_cnt
            total = node.val + left_sum + right_sum
            
            if total // total_cnt == node.val:
                ans += 1
            return (total, total_cnt)
            
        dfs(root)
        return ans