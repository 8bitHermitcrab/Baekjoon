"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        else:
            depth = 0
            queue = [root]
            next_que = []
            
            while queue:
                out = queue.pop(0)
                
                for child in out.children:
                    next_que.append(child)
                
                if queue == []:
                    queue, next_que = next_que, queue
                    depth += 1
            return depth