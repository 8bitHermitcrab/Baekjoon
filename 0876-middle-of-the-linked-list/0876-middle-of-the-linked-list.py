# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        idx = 0
        h = head
        
        while h.next:
            h = h.next
            idx += 1
        
        middle = (idx // 2) + (idx % 2)    
        while middle > 0:
            head = head.next
            middle -= 1
            
        return head