# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1
            # n 레벨의 모든 노드를 pop 하여 -> 인접노드(자식노드)들을 q에 넣는 과정
            for _ in range(len(queue)):
                # deque에서 popleft는 q상의 front를 추출
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 ==> 깊이
        return depth