"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        
        deq = deque()
        deq.append((root, 0))
        
        while deq:
            node, level = deq.popleft()
            
            if node:
                if len(ans) <= level:
                    ans.append([])
                
                ans[level].append(node.val)
                
                for child in node.children:
                    deq.append((child, level + 1))
        
        return ans