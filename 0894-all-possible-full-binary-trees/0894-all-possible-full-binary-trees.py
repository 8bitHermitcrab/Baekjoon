# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        dp[1] = [TreeNode(0)]
        
        def dfs(cnt):
            ans = []
            if cnt in dp:
                return dp[cnt]
            
            for i in range(1, cnt, 2):
                left = dfs(i)
                right = dfs(cnt - i - 1)
                
                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        ans.append(root)
            dp[cnt] = ans
            return ans
        
        return dfs(n)