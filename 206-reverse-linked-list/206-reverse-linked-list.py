# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        
        ptr = head.next
        
        while ptr:
            p1 = ptr
            ptr = ptr.next
            p1.next = temp
            temp = p1
        
        head.next = None
        head = temp
        return head