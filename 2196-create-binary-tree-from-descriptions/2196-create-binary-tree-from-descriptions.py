# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        value = {}
        non_roots = set()
        
        for p, c, isLeft in descriptions:
            if p not in value:
                value[p] = TreeNode(p)
            if c not in value:
                value[c] = TreeNode(c)
            
            parent = value[p]
            child = value[c]
            non_roots.add(c)
            
            if isLeft:
                parent.left = child
            else:
                parent.right = child
                
        for i in value.keys():
            if i not in non_roots:
                return value[i]