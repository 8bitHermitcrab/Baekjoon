# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            left_bal = dfs(node.left)
            right_bal = dfs(node.right)
            
            nonlocal move_cnt
            move_cnt += abs(left_bal) + abs(right_bal)
            return left_bal + right_bal + node.val - 1
        
        move_cnt = 0
        dfs(root)
        return move_cnt