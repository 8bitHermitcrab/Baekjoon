# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        leafs = self.bfs(root)
        return self.lca(root, leafs)
    
    def bfs(self, node):
        que = [node]
        while que:
            level = []

            for i in range(len(que)):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

                level.append(node)

            if not que:
                return level

    def lca(self, node, nodes):
        if not node:
            return None

        if node in nodes:
            return node

        left = self.lca(node.left, nodes)
        right = self.lca(node.right, nodes)

        if left and right:
            return node
        else:
            return left or right