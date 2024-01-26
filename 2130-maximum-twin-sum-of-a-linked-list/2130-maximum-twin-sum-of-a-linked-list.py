# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        pair = []
        while head:
            pair.append(head.val)
            head = head.next
        
        for i in range(len(pair) // 2):
            ans = max(ans, pair[i] + pair[len(pair) - 1 - i])
        return ans